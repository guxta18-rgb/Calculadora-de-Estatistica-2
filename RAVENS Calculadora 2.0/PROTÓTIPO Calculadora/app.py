import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from calculos import (
    limpar_dados_entrada,
    gerar_rol,
    tamanho_amostra,
    tabela_frequencia_simples,
    tabela_frequencia_classes,
    medidas_tendencia_central,
    medidas_dispersao,
    mediana_dados_agrupados,
    histograma_dados,
)


st.set_page_config(
    page_title="Calculadora Estatística Profissional",
    page_icon="📊",
    layout="wide",
)


def aplicar_estilo_dark():
    """Aplica um tema escuro com estética de terminal usando CSS customizado."""
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #050608;
            color: #e5e5e5;
        }
        .stApp {
            background: radial-gradient(circle at top left, #111827, #020617);
        }
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }
        .terminal-panel {
            background-color: #020617;
            border-radius: 8px;
            border: 1px solid #1f2937;
            padding: 1rem 1.25rem;
            font-family: "JetBrains Mono", "Fira Code", monospace;
            color: #e5e7eb;
        }
        .terminal-panel h3, .terminal-panel h4 {
            color: #e5e7eb;
        }
        .terminal-badge {
            background: linear-gradient(90deg, #22c55e, #0ea5e9);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            font-size: 0.75rem;
        }
        .stTextArea textarea {
            background-color: #020617;
            color: #e5e7eb;
            border-radius: 8px;
            border: 1px solid #111827;
            font-family: "JetBrains Mono", monospace;
        }
        .stSelectbox, .stNumberInput, .stButton > button {
            font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .stButton > button {
            background: linear-gradient(90deg, #22c55e, #0ea5e9);
            border: none;
            color: #020617;
            font-weight: 600;
        }
        .stButton > button:hover {
            filter: brightness(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    aplicar_estilo_dark()

    st.markdown(
        "<div class='terminal-badge'>FATEC · Estatística Aplicada</div>",
        unsafe_allow_html=True,
    )
    st.title("📊 Calculadora Estatística Profissional")
    st.caption(
        "Aplicação interativa para análise descritiva de dados – ROL, "
        "tabelas de frequência, medidas de tendência central e dispersão."
    )

    st.sidebar.markdown("### Configurações (Prova)")
    st.sidebar.caption("Ajuste as fórmulas conforme as aulas.")

    metodo_k = st.sidebar.selectbox(
        "Número de classes (k) – Aula II",
        ["Regra de Sturges", "Raiz quadrada de n (k=√n)"],
        index=0,
    )
    arredondar_h = st.sidebar.selectbox(
        "Amplitude da classe (h) – Aula II",
        ["Manter h = AT/k (com decimais)", "Arredondar h para cima (ceil)"],
        index=0,
    )
    tipo_variancia = st.sidebar.selectbox(
        "Variância/Desvio padrão – Aula IV",
        ["Amostral (n-1)", "Populacional (n)"],
        index=0,
    )
    casas_decimais = st.sidebar.number_input(
        "Casas decimais para exibição",
        min_value=0,
        max_value=6,
        value=2,
        step=1,
    )

    with st.container():
        col_input, _col_spacer = st.columns([2, 1])

        with col_input:
            st.subheader("1. Dados de Entrada")
            dados_brutos = st.text_area(
                "Insira os dados numéricos (separados por vírgula ou espaço):",
                height=140,
                placeholder="Exemplos: 10 12 13 15 15 16 18 20\nou: 10, 12, 13, 15, 15, 16, 18, 20",
            )

    st.markdown("---")

    if st.button("Calcular Estatísticas", type="primary"):
        try:
            valores = limpar_dados_entrada(dados_brutos)
        except ValueError as e:
            st.error(str(e))
            return

        metodo_interno = "sturges" if metodo_k.startswith("Regra") else "sqrt"
        arredondar_h_para_cima = arredondar_h.startswith("Arredondar")

        rol = gerar_rol(valores)
        n = tamanho_amostra(valores)

        mtc = medidas_tendencia_central(valores)
        tipo_md = "amostral" if tipo_variancia.startswith("Amostral") else "populacional"
        md = medidas_dispersao(valores, tipo=tipo_md)

        with st.container():
            col_rol, col_mtc, col_md = st.columns([1.2, 1.1, 1.1])

            with col_rol:
                st.markdown("<div class='terminal-panel'>", unsafe_allow_html=True)
                st.markdown("### ROL e Tamanho da Amostra")
                st.write(f"**n (tamanho da amostra)**: {n}")
                st.write("**ROL (dados ordenados)**:")
                st.write(", ".join([f"{v:.{casas_decimais}f}" for v in rol]))
                st.markdown("</div>", unsafe_allow_html=True)

            with col_mtc:
                st.markdown("<div class='terminal-panel'>", unsafe_allow_html=True)
                st.markdown("### Medidas de Tendência Central (MTC)")
                st.write(f"**Média aritmética (x̄)** = {mtc['media']:.{casas_decimais}f}")
                st.write(f"**Mediana** = {mtc['mediana']:.{casas_decimais}f}")

                if mtc["tipo_moda"] == "amodal":
                    st.write("**Moda**: Amodal (nenhum valor se repete).")
                else:
                    modas_fmt = ", ".join(
                        f"{m:.{casas_decimais}f}" for m in mtc["modas"]
                    )
                    st.write(
                        f"**Moda** ({mtc['tipo_moda']}): {modas_fmt} "
                        f"(valor(es) mais frequente(s))."
                    )
                st.markdown("</div>", unsafe_allow_html=True)

            with col_md:
                st.markdown("<div class='terminal-panel'>", unsafe_allow_html=True)
                st.markdown("### Medidas de Dispersão (MD)")
                st.write(
                    f"**Amplitude Total (AT)** = xmax - xmin = "
                    f"{valores.max():.{casas_decimais}f} - {valores.min():.{casas_decimais}f} "
                    f"= {md['AT']:.{casas_decimais}f}"
                )
                if md["tipo"] == "populacional":
                    st.write(
                        f"**Variância populacional (σ²)** = Σ(xᵢ - μ)² / n "
                        f"= {md['variancia']:.{casas_decimais}f}"
                    )
                    st.write(
                        f"**Desvio padrão populacional (σ)** = √σ² "
                        f"= {md['desvio_padrao']:.{casas_decimais}f}"
                    )
                else:
                    st.write(
                        f"**Variância amostral (s²)** = Σ(xᵢ - x̄)² / (n - 1) "
                        f"= {md['variancia']:.{casas_decimais}f}"
                    )
                    st.write(
                        f"**Desvio padrão amostral (s)** = √s² "
                        f"= {md['desvio_padrao']:.{casas_decimais}f}"
                    )
                st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

        # Tabelas de distribuição de frequência
        st.subheader("3. Tabelas de Distribuição de Frequência")

        col_tab1, col_tab2 = st.columns(2)

        with col_tab1:
            st.markdown("#### Sem Intervalos de Classe (Variável Discreta)")
            df_simples = tabela_frequencia_simples(valores)
            df_simples_fmt = df_simples.copy()
            df_simples_fmt["xi"] = df_simples_fmt["xi"].round(casas_decimais)
            df_simples_fmt["fr_%"] = df_simples_fmt["fr_%"].round(2)
            df_simples_fmt["Fr_%"] = df_simples_fmt["Fr_%"].round(2)
            st.dataframe(df_simples_fmt, use_container_width=True)

        with col_tab2:
            st.markdown("#### Com Intervalos de Classe (Variável Contínua)")
            try:
                df_classes = tabela_frequencia_classes(
                    valores,
                    metodo_k=metodo_interno,
                    arredondar_h_para_cima=arredondar_h_para_cima,
                )
                df_classes_fmt = df_classes.copy()
                df_classes_fmt["li"] = df_classes_fmt["li"].round(casas_decimais)
                df_classes_fmt["ls"] = df_classes_fmt["ls"].round(casas_decimais)
                df_classes_fmt["xi"] = df_classes_fmt["xi"].round(casas_decimais)
                df_classes_fmt["fr_%"] = df_classes_fmt["fr_%"].round(2)
                df_classes_fmt["Fr_%"] = df_classes_fmt["Fr_%"].round(2)
                st.dataframe(df_classes_fmt, use_container_width=True)

                at_info = df_classes.attrs.get("AT")
                k_info = df_classes.attrs.get("k")
                h_info = df_classes.attrs.get("h")
                if at_info is not None:
                    st.caption(
                        f"AT = {at_info:.{casas_decimais}f} · "
                        f"k = {k_info} · h ≈ {h_info:.{casas_decimais}f}"
                    )

                # Mediana para dados agrupados (Aula IV)
                med_agr = mediana_dados_agrupados(df_classes, n=n, h=float(h_info))
                st.markdown("**Mediana (dados agrupados)**")
                st.write(
                    f"Classe da mediana: **{med_agr['classe_mediana']}** "
                    f"(Fi ≥ n/2 = {med_agr['posicao']:.{casas_decimais}f})"
                )
                st.write(
                    "Fórmula: **Me = li + [((n/2) − Fant) / fme] · h**"
                )
                st.write(
                    f"Substituindo: Me = {med_agr['li']:.{casas_decimais}f} + "
                    f"((({med_agr['posicao']:.{casas_decimais}f} − {med_agr['Fant']}) / {med_agr['fme']}) · "
                    f"{med_agr['h']:.{casas_decimais}f})"
                )
                st.write(
                    f"Resultado: **Me ≈ {med_agr['mediana_agrupada']:.{casas_decimais}f}**"
                )
            except ValueError as e:
                st.warning(str(e))

        st.markdown("---")

        # Visualizações: Histograma e Gráfico de Setores
        st.subheader("4. Visualizações Gráficas")
        aba_hist, aba_pizza = st.tabs(["Histograma", "Gráfico de Setores (Pizza)"])

        with aba_hist:
            st.markdown("##### Histograma dos Dados")
            counts, bin_edges = histograma_dados(valores, metodo_k=metodo_interno)
            centros = 0.5 * (bin_edges[:-1] + bin_edges[1:])

            fig, ax = plt.subplots(figsize=(6, 3.5))
            ax.bar(centros, counts, width=(bin_edges[1] - bin_edges[0]) * 0.9, color="#22c55e")
            ax.set_facecolor("#020617")
            fig.patch.set_facecolor("#020617")
            ax.set_xlabel("Classes")
            ax.set_ylabel("Frequência")
            ax.grid(True, color="#111827", linestyle="--", linewidth=0.5, alpha=0.7)
            ax.tick_params(colors="#e5e7eb")
            ax.spines["bottom"].set_color("#e5e7eb")
            ax.spines["left"].set_color("#e5e7eb")
            st.pyplot(fig, use_container_width=True)

        with aba_pizza:
            st.markdown("##### Gráfico de Setores (Frequência Relativa)")
            df_freq = tabela_frequencia_simples(valores)
            labels = [f"{xi:.{casas_decimais}f}" for xi in df_freq["xi"]]
            sizes = df_freq["fi"].values

            fig2, ax2 = plt.subplots(figsize=(5, 5))
            wedges, texts, autotexts = ax2.pie(
                sizes,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90,
                textprops={"color": "#e5e7eb"},
            )
            ax2.set_facecolor("#020617")
            fig2.patch.set_facecolor("#020617")
            for w in wedges:
                w.set_edgecolor("#020617")
            st.pyplot(fig2, use_container_width=False)


if __name__ == "__main__":
    main()

