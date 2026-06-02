import numpy as np
import pandas as pd
from math import ceil, log10, sqrt


def limpar_dados_entrada(texto: str) -> np.ndarray:
    """
    Converte uma string de entrada em um array NumPy de floats.

    Regras:
    - Aceita números separados por vírgula ou espaço.
    - Ignora strings vazias após o split.
    - Lança ValueError se existir qualquer valor não numérico.
    """
    if not texto or texto.strip() == "":
        raise ValueError("Nenhum dado foi informado.")

    # Substitui vírgulas por espaços para tratar ambos os separadores
    bruto = texto.replace(",", " ")
    partes = [p for p in bruto.split() if p.strip() != ""]

    if not partes:
        raise ValueError("Nenhum número válido foi encontrado na entrada.")

    valores = []
    for p in partes:
        try:
            valores.append(float(p.replace(",", ".")))
        except ValueError as exc:
            raise ValueError(f"Valor inválido encontrado: '{p}'. Use apenas números.") from exc

    if len(valores) < 2:
        raise ValueError("Informe pelo menos dois valores para análise estatística.")

    return np.array(valores, dtype=float)


def gerar_rol(valores: np.ndarray) -> np.ndarray:
    """Retorna o ROL (dados ordenados em ordem crescente)."""
    return np.sort(valores)


def tamanho_amostra(valores: np.ndarray) -> int:
    """Retorna o tamanho da amostra n."""
    return int(valores.size)


def tabela_frequencia_simples(valores: np.ndarray) -> pd.DataFrame:
    """
    Gera tabela de distribuição de frequência sem intervalos de classe
    (adequada para variáveis discretas).

    Colunas:
    - xi: valor observado
    - fi: frequência absoluta
    - fr_%: frequência relativa em %
    - Fi: frequência acumulada
    - Fr_%: frequência relativa acumulada em %
    """
    n = tamanho_amostra(valores)
    serie = pd.Series(valores)
    freq_abs = serie.value_counts().sort_index()

    df = pd.DataFrame({"xi": freq_abs.index.astype(float), "fi": freq_abs.values.astype(int)})
    df["fr_%"] = (df["fi"] / n) * 100
    df["Fi"] = df["fi"].cumsum()
    df["Fr_%"] = (df["Fi"] / n) * 100

    return df.reset_index(drop=True)


def _calcular_k(n: int, metodo: str = "sturges") -> int:
    """
    Calcula o número de classes k (Aula II).

    - Regra de Sturges: k = 1 + 3,3 * log10(n)
    - Raiz quadrada de n: k = sqrt(n)

    Observação didática:
    - Usamos arredondamento para cima (ceil) para obter um número inteiro de classes.
    """
    if metodo == "sqrt":
        k = ceil(sqrt(n))
    else:
        k = ceil(1 + 3.3 * log10(n))
    return max(k, 1)


def _calcular_h(at: float, k: int, arredondar_para_cima: bool = False) -> float:
    """
    Calcula a amplitude de classe h (Aula II).

    Fórmula:
    - h = AT / k

    Opção:
    - Se arredondar_para_cima=True, aplica ceil(h) (arredonda para cima).
      Essa escolha é comum quando a aula pede intervalos "inteiros" e fáceis de ler.
    """
    if k <= 0:
        raise ValueError("k deve ser maior que zero.")
    h = at / k
    if arredondar_para_cima:
        h = float(ceil(h))
    return float(h)


def tabela_frequencia_classes(
    valores: np.ndarray,
    metodo_k: str = "sturges",
    arredondar_h_para_cima: bool = False,
) -> pd.DataFrame:
    """
    Gera tabela de distribuição de frequência com intervalos de classe
    (adequada para variáveis contínuas).

    Passos principais:
    - Amplitude Total AT = xmax - xmin
    - Número de classes k (Sturges ou raiz de n)
    - Amplitude do intervalo h = AT / k
      - opcionalmente, h pode ser arredondado para cima (ceil)
    - Ponto médio xi = (LimiteInferior + LimiteSuperior) / 2

    Colunas:
    - classe: intervalo textual, ex: [a, b)
    - li: limite inferior da classe
    - ls: limite superior da classe
    - xi: ponto médio
    - fi: frequência absoluta
    - fr_%: frequência relativa em %
    - Fi: frequência acumulada
    - Fr_%: frequência relativa acumulada em %
    """
    n = tamanho_amostra(valores)
    vmin, vmax = float(valores.min()), float(valores.max())
    at = vmax - vmin
    if at == 0:
        raise ValueError("Todos os valores são idênticos; não é possível criar classes.")

    k = _calcular_k(n, metodo_k)
    h = _calcular_h(at, k, arredondar_para_cima=arredondar_h_para_cima)
    if h == 0:
        raise ValueError("Amplitude de classe h inválida.")

    # Limites de classe baseados em h para manter fidelidade à fórmula h=AT/k
    # Garante inclusão do máximo com um pequeno epsilon no último limite.
    limites = np.array([vmin + i * h for i in range(k + 1)], dtype=float)
    if limites[-1] < vmax:
        # Se h foi arredondado para cima, é normal limites[-1] >= vmax;
        # mas se por flutuação ficou abaixo, ajustamos para incluir vmax.
        limites[-1] = vmax
    limites[-1] = limites[-1] + 1e-9

    # Cria rótulos textuais das classes no formato [a, b)
    classes_labels = []
    li_list = []
    ls_list = []
    for i in range(k):
        a = limites[i]
        b = limites[i + 1]
        li_list.append(float(a))
        ls_list.append(float(b))
        classes_labels.append(f"[{a:.2f}, {b:.2f})")

    # Classificação dos dados em intervalos usando pandas.cut
    categorias = pd.cut(valores, bins=limites, include_lowest=True, right=False)
    freq_abs = categorias.value_counts().sort_index()

    df = pd.DataFrame(
        {
            "classe": classes_labels,
            "li": li_list,
            "ls": ls_list,
            "fi": freq_abs.values.astype(int),
        }
    )

    # Pontos médios xi
    df["xi"] = (df["li"] + df["ls"]) / 2

    df["fr_%"] = (df["fi"] / n) * 100
    df["Fi"] = df["fi"].cumsum()
    df["Fr_%"] = (df["Fi"] / n) * 100

    # Inclui informações auxiliares como atributos
    df.attrs["AT"] = at
    df.attrs["k"] = k
    df.attrs["h"] = h
    df.attrs["limites"] = limites

    return df


def medidas_tendencia_central(valores: np.ndarray) -> dict:
    """
    Calcula Medidas de Tendência Central:
    - Média aritmética: soma(xi) / n
    - Mediana: valor central (ou média dos dois centrais) após ordenar
    - Moda: valor(es) mais frequente(s)
    """
    n = tamanho_amostra(valores)
    media = float(np.mean(valores))
    mediana = float(np.median(valores))

    serie = pd.Series(valores)
    freq = serie.value_counts()
    max_freq = freq.max()

    # Se todos aparecem uma única vez, consideramos amodal
    if max_freq == 1:
        tipo_moda = "amodal"
        modas = []
    else:
        modas = sorted(freq[freq == max_freq].index.tolist())
        if len(modas) == 1:
            tipo_moda = "unimodal"
        else:
            tipo_moda = "multimodal"

    return {
        "n": n,
        "media": media,
        "mediana": mediana,
        "modas": modas,
        "tipo_moda": tipo_moda,
    }


def mediana_dados_agrupados(df_classes: pd.DataFrame, n: int, h: float) -> dict:
    """
    Calcula a Mediana para Dados Agrupados em Classes (Aula IV), usando:

        Me = li + [ ((n/2) - Fant) / fme ] * h

    Onde:
    - li: limite inferior da classe da mediana
    - Fant: frequência acumulada anterior à classe da mediana
    - fme: frequência da classe da mediana
    - h: amplitude da classe

    Retorna um dicionário com o valor da mediana e os termos da fórmula
    para exibição didática na interface.
    """
    if df_classes.empty:
        raise ValueError("Tabela de classes vazia.")
    if "Fi" not in df_classes.columns or "fi" not in df_classes.columns:
        raise ValueError("Tabela de classes precisa conter colunas fi e Fi.")
    if "li" not in df_classes.columns:
        raise ValueError("Tabela de classes precisa conter o limite inferior (li).")
    if n <= 0:
        raise ValueError("n inválido.")
    if h <= 0:
        raise ValueError("h inválido.")

    pos = n / 2
    idx = int((df_classes["Fi"] >= pos).idxmax())

    fi = int(df_classes.loc[idx, "fi"])
    if fi == 0:
        raise ValueError("A classe da mediana tem fi=0; verifique os dados/intervalos.")

    li = float(df_classes.loc[idx, "li"])
    Fant = int(df_classes.loc[idx - 1, "Fi"]) if idx > 0 else 0

    me = li + (((pos - Fant) / fi) * h)

    return {
        "mediana_agrupada": float(me),
        "li": li,
        "Fant": Fant,
        "fme": fi,
        "h": float(h),
        "posicao": float(pos),
        "classe_mediana": str(df_classes.loc[idx, "classe"]),
        "indice_classe": idx,
    }


def medidas_dispersao(valores: np.ndarray, tipo: str = "amostral") -> dict:
    """
    Calcula Medidas de Dispersão:
    - Amplitude Total AT = xmax - xmin
    - Variância e desvio padrão (Aula IV):
      - Populacional: σ² = Σ(xi - μ)² / n   e   σ = √σ²
      - Amostral:     s² = Σ(xi - x̄)² / (n-1) e s = √s²
    """
    n = tamanho_amostra(valores)
    vmin, vmax = float(valores.min()), float(valores.max())
    at = vmax - vmin

    if tipo == "populacional":
        ddof = 0
        variancia_label = "populacional"
    else:
        ddof = 1
        variancia_label = "amostral"

    variancia = float(np.var(valores, ddof=ddof))
    desvio_padrao = float(np.sqrt(variancia))

    return {
        "n": n,
        "AT": at,
        "variancia": variancia,
        "desvio_padrao": desvio_padrao,
        "tipo": variancia_label,
    }


def histograma_dados(
    valores: np.ndarray,
    bins: int | None = None,
    metodo_k: str = "sturges",
):
    """
    Retorna dados de histograma usando NumPy.

    - counts: frequências em cada classe
    - bin_edges: limites dos intervalos
    """
    if bins is None:
        bins = _calcular_k(tamanho_amostra(valores), metodo=metodo_k)
    counts, bin_edges = np.histogram(valores, bins=bins)
    return counts, bin_edges

