# ⚡ StatLab — Laboratório de Estatística Descritiva

> **Dark mode. Terminal vibe. Precisão estatística real.**  
> O **StatLab** é uma calculadora estatística descritiva com estética neon moderna, criada para unir visual técnico, usabilidade e rigor matemático em um fluxo único de análise.

---

## 🟢 Visão Geral

O StatLab foi projetado para dois cenários clássicos de análise:

- **Dados Brutos (não agrupados)**: cálculo ponto a ponto, ideal para resultados exatos.
- **Dados Agrupados (com classes)**: cálculo por distribuição de frequências, ideal para visão resumida com técnicas clássicas (Sturges e Czuber).

Essa separação torna o projeto excelente para:

- estudantes de ADS, Estatística e áreas afins;
- profissionais que precisam validar cálculos manualmente;
- demonstrações didáticas de estatística descritiva;
- comparação entre resultados exatos e aproximados.

 ## 🚀 Demo

🔗 **Clique aqui  https://guxta18-rgb.github.io/Calculadora-de-Estatistica-2/**
</p>

---

## 💻 Identidade Visual e Estética

O projeto adota uma identidade visual forte e coerente:

- 🌑 **Dark mode integral** para conforto visual e foco.
- 🟢 **Neon verde/ciano** em bordas, destaques e feedback visual.
- ⌨️ **Mood terminal/cyber-lab** com tipografia e microdetalhes retro-futuristas.
- 📟 **Cards com tooltips** para leitura rápida de fórmulas e interpretação.
- 📊 **Layout técnico modular** que organiza entrada, tabela e resultados sem poluição.

Essa estética não é apenas “bonita”: ela reforça a sensação de laboratório analítico, ajudando o usuário a interpretar dados com confiança.

---

## 🧪 Diferenciais do StatLab

### 1) Precisão em Dados Brutos

No módulo de dados brutos, os indicadores principais são calculados diretamente do array original:

- Média aritmética exata: \(\bar{X} = \frac{\sum X_i}{n}\)
- Variância e desvio com seletor:
  - **Amostra (n−1)**
  - **População (n)**

✅ Isso evita erro de arredondamento causado por agrupamento em classes.

### 2) Poder de síntese em Dados Agrupados

No módulo de tabela de frequências:

- classes com limites inferior/superior + frequência \(f_i\);
- ponto médio \(X_i\);
- média ponderada;
- moda de Czuber;
- mediana para classes;
- variância e desvio agrupados.

✅ Ideal para cenários de distribuição resumida e análise por faixas.

### 3) Ponte automática via Sturges

A partir dos dados brutos, o botão **“Sugerir Classes (Sturges)”**:

- calcula \(AA\), \(k\) e \(h\);
- monta intervalos automaticamente;
- estima frequências por intervalo;
- preenche a tabela agrupada com 1 clique.

✅ Ganho de produtividade e consistência metodológica.

---

## 📊 Funcionalidades Detalhadas

## Dados Brutos (não agrupados)

- ✅ ROL (ordenação crescente)
- ✅ Média aritmética
- ✅ Mediana
- ✅ Moda (inclui multimodalidade)
- ✅ Quartis \(Q1, Q2, Q3\)
- ✅ Outliers via IQR
- ✅ Variância (amostral/populacional)
- ✅ Desvio padrão (amostral/populacional)
- ✅ Coeficiente de variação (CV)
- ✅ Min, Máx, n e Amplitude amostral (AA)

## Organização por classes (Sturges)

- ✅ Regra de Sturges para número de classes
- ✅ Cálculo de amplitude de classe
- ✅ Geração automática dos intervalos
- ✅ Contagem de frequências por intervalo
- ✅ Resumo instantâneo com \(AA\), \(k\) e \(h\)

## Dados Agrupados (tabela de frequências)

- ✅ Entrada manual por classe \([LI, LS)\)
- ✅ Frequência absoluta \(f_i\)
- ✅ Frequência acumulada \(F_i\)
- ✅ Frequência relativa \(%\)
- ✅ Ponto médio \(X_i\)
- ✅ Produtos \(f_iX_i\) e \(f_iX_i^2\)
- ✅ Média ponderada
- ✅ Moda de Czuber
- ✅ Mediana agrupada
- ✅ Variância e desvio padrão agrupados
- ✅ Coeficiente de variação agrupado

---

## 🧭 Guia de Uso (Passo a Passo)

## Fluxo A — Dados Brutos (resultado exato)

1. Abra a aba **Dados Brutos**.
2. Cole os valores no campo de entrada (separados por espaço ou vírgula).
3. Escolha a base de dispersão:
   - **Amostra (n-1)** ou
   - **População (n)**.
4. Clique em **Calcular Dados Brutos**.
5. Analise:
   - cards de tendência central;
   - card de dispersão em destaque;
   - quartis e outliers;
   - ROL completo.

## Fluxo B — Sugestão de classes por Sturges

1. Com dados brutos preenchidos, clique em **Sugerir Classes (Sturges)**.
2. O sistema:
   - calcula parâmetros \(AA, k, h\);
   - preenche automaticamente a aba de tabela.
3. Vá para a aba **Tabela de Frequências** para revisar/editar.
4. Clique em **Calcular Tabela**.

## Fluxo C — Entrada manual agrupada

1. Abra a aba **Tabela de Frequências**.
2. Adicione/remova linhas de classes.
3. Preencha:
   - limite inferior;
   - limite superior;
   - frequência \(f_i\).
4. Clique em **Calcular Tabela**.
5. Interprete os resultados agrupados nos cards e na tabela.

---

## 🧠 Categorias de Cálculo e Arquitetura Modular

O script principal foi estruturado em módulos sem dependências externas:

| Módulo | Responsabilidade | Saída principal |
|---|---|---|
| `Utils` | parse, formatação e arredondamento | dados normalizados para UI |
| `ModuloDadosBrutos` | estatística exata do array original | métricas exatas (incl. quartis/outliers) |
| `ModuloOrganizacao` | regras de Sturges e intervalos | \(AA\), \(k\), \(h\), classes sugeridas |
| `ModuloDadosAgrupados` | estatística por frequências | tabela derivada + medidas agrupadas |
| `UI` | controle de abas, validação e render | cards, tabela e mensagens |

### Filosofia da implementação

- **Separação entre cálculo e interface**;
- **Funções pequenas e legíveis**;
- **Baixo acoplamento entre módulos**;
- **Didático para estudo acadêmico**;
- **Pronto para evolução futura** (exportação, gráficos, testes unitários etc.).

---

## 📚 Dicionário de Fórmulas

> Notação amigável usada no projeto.

### Dados Brutos

**Média**

\[
\bar{X} = \frac{\sum_{i=1}^{n} X_i}{n}
\]

**Variância Populacional**

\[
\sigma^2 = \frac{\sum_{i=1}^{n}(X_i-\bar{X})^2}{n}
\]

**Variância Amostral**

\[
S^2 = \frac{\sum_{i=1}^{n}(X_i-\bar{X})^2}{n-1}
\]

**Desvio Padrão**

\[
\sigma = \sqrt{\sigma^2}
\quad\text{ou}\quad
S = \sqrt{S^2}
\]

**Coeficiente de Variação**

\[
CV = \left(\frac{S}{\bar{X}}\right)\times 100
\]

**Amplitude Amostral**

\[
AA = X_{\max} - X_{\min}
\]

### Organização de Classes

**Regra de Sturges**

\[
k = 1 + 3.322\cdot\log_{10}(n)
\]

**Amplitude de Classe**

\[
h = \frac{AA}{k}
\]

### Dados Agrupados

**Ponto Médio da Classe**

\[
X_i = \frac{LI + LS}{2}
\]

**Média Ponderada**

\[
\bar{X} = \frac{\sum (X_i\cdot f_i)}{n}
\]

**Moda de Czuber**

\[
Mo = l_{mo} + \left[\frac{f_{mo}-f_{ant}}{2f_{mo}-f_{ant}-f_{pos}}\right]\cdot h
\]

**Mediana Agrupada**

\[
Md = l_{md} + \left[\frac{\frac{n}{2}-F_{ant}}{f_{md}}\right]\cdot h
\]

**Variância Agrupada**

\[
S^2 = \frac{\sum(f_i\cdot X_i^2)}{n} - \bar{X}^2
\]

---

## 🧩 Trechos Reais de Código (Módulos JS)

### `ModuloDadosBrutos` (base exata, com amostra/população)

```js
variancia(dados, media, tipo = 'amostra') {
  const somaQuadrados = dados.reduce((acc, v) => acc + Math.pow(v - media, 2), 0);
  if (tipo === 'amostra') {
    if (dados.length < 2) throw new Error('Para cálculo amostral são necessários pelo menos 2 valores.');
    return somaQuadrados / (dados.length - 1);
  }
  return somaQuadrados / dados.length;
}
```

```js
calcular(dados, tipoDispersao = 'amostra') {
  const ordenados = [...dados].sort((a, b) => a - b);
  const media = this.media(dados);
  const variancia = this.variancia(dados, media, tipoDispersao);
  const desvioPadrao = Math.sqrt(variancia);
  // ...
}
```

### `ModuloOrganizacao` (Sturges + classes)

```js
sturges(dados) {
  const n = dados.length;
  const min = Math.min(...dados);
  const max = Math.max(...dados);
  const AA = max - min;
  const k = Math.max(1, Math.ceil(1 + 3.322 * Math.log10(n)));
  const h = AA === 0 ? 1 : AA / k;
  return { n, min, max, AA, k, h };
}
```

### `ModuloDadosAgrupados` (média ponderada + Czuber)

```js
media(tabela, n) {
  return tabela.reduce((acc, l) => acc + l.fixi, 0) / n;
}
```

```js
modaCzuber(tabela) {
  const indiceModa = tabela.reduce((maxIdx, linha, idx, arr) => (linha.fi > arr[maxIdx].fi ? idx : maxIdx), 0);
  const modal = tabela[indiceModa];
  const fant = indiceModa > 0 ? tabela[indiceModa - 1].fi : 0;
  const fpos = indiceModa < tabela.length - 1 ? tabela[indiceModa + 1].fi : 0;
  const h = modal.ls - modal.li;
  const denom = (2 * modal.fi) - fant - fpos;
  const moda = denom === 0 ? modal.xi : modal.li + ((modal.fi - fant) / denom) * h;
  return { moda, indiceModa };
}
```

### `UI` (integração entre abas e cálculo)

```js
calcularBrutos() {
  const dados = this.lerBrutos();
  const tipoDispersao = this.obterTipoDispersaoBrutos();
  const brutos = ModuloDadosBrutos.calcular(dados, tipoDispersao);
  // cards exatos de dados brutos
}
```

---

## 🚀 Instalação e Execução

Como o projeto é **Vanilla HTML + JS + Tailwind via CDN**, rodar é simples:

## Opção 1 — Abrir direto no navegador

1. Baixe/clone o projeto.
2. Abra o arquivo principal (`dashboard-estatistico.html`) no navegador.
3. Pronto: já funciona.

## Opção 2 — Live Server (recomendado para desenvolvimento)

1. Abra a pasta no VS Code/Cursor.
2. Instale a extensão **Live Server** (se quiser hot reload).
3. Clique em **Open with Live Server**.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Papel no projeto |
|---|---|---|
| Estrutura | HTML5 | layout e semântica da interface |
| Estilo | CSS3 + variáveis | tema dark neon e componentes visuais |
| UI Utility | Tailwind CSS (CDN) | apoio rápido de utilitários |
| Lógica | JavaScript Puro (ES6+) | cálculos estatísticos e modularização |
| Tipografia | Google Fonts: Share Tech Mono + DM Sans | identidade terminal + legibilidade |

---

## 🔍 Interpretação dos Resultados

### Quando usar Dados Brutos

Use quando você precisa de:

- conferência precisa com cálculo manual;
- valores exatos de média/variância/desvio;
- análise de outliers e quartis sem aproximação.

### Quando usar Dados Agrupados

Use quando você precisa de:

- visão resumida de distribuição;
- análise por faixa/classe;
- apresentação tabular em contextos didáticos.

---

## ✅ Qualidade Matemática e Objetivo de Exatidão

O StatLab foi pensado para evitar confusão comum em estatística aplicada:

- **Média dos cards de dados brutos**: sempre calculada do array original.
- **Dispersão amostral/populacional**: escolha explícita via toggle.
- **Resultados agrupados**: tratados como aproximações por classes (não substituem os exatos quando a exigência é precisão ponto a ponto).

Esse desenho garante consistência para cenários como:

- bases com 200+ valores;
- validação acadêmica com correção manual;
- comparação entre métodos.

---

## 🧱 Estrutura Atual do Projeto (resumo)

```text
.
├── dashboard-estatistico.html
└── README.md
```

> Toda a lógica atual está concentrada no arquivo principal para facilitar portabilidade.  
> Em evolução futura, pode ser separado em `js/modules/` e `css/`.

---

## 🧭 Roadmap Sugerido

- [ ] Exportação de relatório em PDF
- [ ] Importação de CSV/XLSX
- [ ] Gráficos (histograma, boxplot, curva acumulada)
- [ ] Testes unitários para fórmulas críticas
- [ ] Modo docente (explicação passo a passo das contas)
- [ ] Internacionalização (PT/EN/ES)

---

## 🤝 Público-Alvo

- 👨‍🎓 Estudantes de ADS, Estatística, Engenharia e áreas de dados
- 👩‍🏫 Professores que precisam de ferramenta didática visual
- 👨‍💼 Analistas que desejam validação rápida de cálculos descritivos
- 🧠 Pessoas que valorizam precisão matemática com UX moderna

---

## 🧾 Licença e Uso

Defina aqui sua licença preferida (ex.: MIT) para facilitar reuso acadêmico e profissional.

Exemplo:

```txt
MIT License
Copyright ...
```

---

## 🔚 Conclusão

O **StatLab** combina:

- rigor estatístico;
- organização modular;
- visual técnico diferenciado;
- excelente valor didático.

Se você busca uma base sólida para aprender, ensinar ou evoluir uma calculadora estatística moderna, este projeto entrega um ponto de partida de alto nível. ⚡📊

