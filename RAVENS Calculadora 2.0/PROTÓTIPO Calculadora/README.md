## Calculadora Estatística Profissional (Streamlit)

Aplicação web em Python para análise estatística descritiva, desenvolvida para a disciplina de **Estatística Aplicada (FATEC)**.

### Funcionalidades

- **Tratamento de dados**
  - Entrada de dados numéricos separados por vírgula ou espaço.
  - Geração do **ROL** (dados ordenados).
  - Cálculo do **tamanho da amostra (n)**.

- **Tabelas de distribuição de frequência**
  - **Sem intervalos de classe** (variáveis discretas).
  - **Com intervalos de classe** (variáveis contínuas), com:
    - Amplitude Total (AT)
    - Número de classes (k) pela **regra de Sturges** ou **raiz de n**
    - Amplitude do intervalo (h)
  - Colunas: `Classe`, `xi` (ponto médio), `fi` (freq. absoluta), `fr %` (freq. relativa), `Fi` (freq. acumulada) e `Fr %` (freq. acumulada relativa).

- **Medidas de Tendência Central (MTC)**
  - Média aritmética
  - Mediana
  - Moda (identificando se é amodal, unimodal ou multimodal)

- **Medidas de Dispersão (MD)**
  - Amplitude Total
  - Variância amostral
  - Desvio padrão amostral

- **Visualizações**
  - Histograma dos dados
  - Gráfico de setores (pizza) da distribuição de frequências
  - Interface em **dark mode / estilo terminal** (via CSS personalizado).

### Estrutura do projeto

- `calculos.py` – toda a lógica de estatística (cálculos com **NumPy** e **Pandas**).
- `app.py` – interface web em **Streamlit**, chamando as funções de `calculos.py`.
- `requirements.txt` – dependências do projeto.

### Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação Streamlit:

```bash
streamlit run app.py
```

4. O navegador abrirá automaticamente em `http://localhost:8501` com a calculadora.

