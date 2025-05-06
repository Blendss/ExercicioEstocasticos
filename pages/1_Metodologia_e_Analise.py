import streamlit as st

st.set_page_config(page_title="Metodologia e Análises", page_icon="📄")

st.title("📄 Metodologia e Contexto")


st.header("Introdução")

st.markdown("""
Neste trabalho, realizamos uma análise exploratória e estatística dos microdados do 
Exame Nacional do Ensino Médio (ENEM) do ano de 2018, com o objetivo de investigar 
possíveis padrões, correlações e comportamentos estocásticos entre diferentes 
variáveis, como as notas por área do conhecimento, características 
sociodemográficas dos participantes e fatores institucionais.
Utilizando técnicas de regressão linear e testes de hipóteses, exploramos relações 
entre notas de disciplinas específicas — como matemática e redação — com a 
intenção de verificar a existência de dependências estatísticas, distribuição dos 
resíduos, homocedasticidade e normalidade. Também aplicamos transformações 
logarítmicas para estabilizar a variância dos erros e avaliamos a aderência dos 
resíduos à distribuição normal por meio de gráficos de quantis (QQ Plot).
Essa análise nos permitiu aplicar conceitos fundamentais dos processos estocásticos 
na prática, como variáveis aleatórias, distribuição de probabilidade e comportamento 
dos erros. Ao final, refletimos sobre a adequação do modelo e os possíveis fatores 
ocultos que influenciam o desempenho dos alunos, propondo caminhos para estudos 
mais robustos em políticas públicas de educação.
""")


# ========================
# Seção: Limpeza de Dados
# ========================
st.header("🧹 Limpeza de Dados")

st.markdown("""
**Colunas mantidas:**  
`'NU_INSCRICAO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_COR_RACA',  
'SG_UF_ESC', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',  
'NU_NOTA_REDACAO', 'Q001', 'Q002', 'Q006', 'Q025', 'Q027',  
'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT'`
""")

st.markdown("""
**Tamanho do arquivo antes:** 2473.05 MB  
**Tamanho do arquivo depois (CSV):** 373.79 MB  
**Tamanho do aquivo depois (Parquet):** 185.90 MB
""")

st.markdown("""
**Presenças nas provas:**
- Faltaram Dia 1 e foram Dia 2: 11.356 (0.27%)  
- Foram Dia 1 e faltaram Dia 2: 254.521 (6.12%)  
- Faltaram nos dois dias: 1.354.127 (32.55%)
""")

st.markdown("""
**Duas colunas adicionadas:**
- TP_ESCOLA / Tipo de escola do Ensino Médio	
- IN_TREINEIRO / Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos 
- Tamanho do arquivo depois (Parquet + duas colunas novas): 185.90 MB
""")

st.markdown("""
**Nova amostra (apenas alunos presentes no dia 1 e dia 2):**
Linhas antes do filtro: 5513733
Linhas após o filtro (só presentes nos dois dias): 3893729
Redução de: 1620004 linhas (29.38%)
Tamanho depois do filtro (Parquet): 135.58 MB

Tamanho do arquivo amostrado: 23.74 MB
Total de linhas na amostra anterior: 24000
Total de linhas originais: 3893729
Total de linhas na amostra: 660554
Fração usada: 0.1696
""")

st.header("Conclusão")

st.markdown("""
A análise dos microdados do ENEM 2018, com uma amostra de 660 mil estudantes, permitiu identificar padrões significativos e desigualdades educacionais relacionadas ao desempenho nas diferentes áreas do conhecimento, considerando variáveis socioeconômicas, demográficas e de infraestrutura. Os resultados reforçam a influência de fatores externos no desempenho dos participantes, evidenciando disparidades que vão além da capacidade individual.
Principais Achados
Desempenho por Estado

MG destacou-se com a maior média em Matemática (558,51), enquanto RR teve a menor média em Redação (460,43).

DF liderou em Ciências da Natureza (509,56), enquanto AC apresentou o pior desempenho médio (466,1).

MG também registrou a maior diferença entre escolas públicas e privadas em Matemática (138,99 pontos), reforçando a desigualdade educacional.

Influência Socioeconômica

Alunos de escolas privadas tiveram desempenho superior, especialmente em Redação (665,18) e Matemática (619,19).

A faixa de renda "Q" apresentou a maior média em Ciências da Natureza (587,98), enquanto a renda "G" foi a mais comum entre o top 10% em Matemática (6.647 participantes).

O acesso à internet influenciou significativamente as notas:

Matemática: Diferença de 54,55 pontos (548,85 vs. 494,30).

Redação: Diferença de 88,46 pontos (537,39 vs. 448,93).

Fatores Demográficos

Sexo:

Homens tiveram maior média em Linguagens (532,62) e Matemática (diferença de 42,31 pontos).

Mulheres lideraram na mediana de Redação (520,00) e representaram 7,27% das notas acima de 800.

Cor/Raça:

Brancos tiveram a maior média em Ciências Humanas (589,73).

Pardos foram o grupo mais numeroso (303.620 participantes).

Indígenas tiveram a menor mediana em Redação (420).

Variabilidade e Correlações

Redação foi a nota mais variável (DP = 184,44), possivelmente devido à subjetividade da correção.

A maior correlação foi entre Linguagens e Ciências Humanas (0,699), indicando habilidades interdisciplinares.

Apenas 0,0017% dos participantes atingiram nota 1000 em Redação, mostrando a raridade da pontuação máxima.

Idade e Escolaridade dos Pais

A faixa etária mais comum foi 17 anos (127.643 participantes), também predominante no top 10% em Matemática (15.735).

A escolaridade dos pais impactou a Redação:

Diferença de 225,4 pontos (pai) e 209,7 pontos (mãe) entre extremos.

Considerações Finais
Os resultados confirmam que desigualdades estruturais – como renda, tipo de escola, acesso à internet e região – têm forte impacto no desempenho no ENEM. A análise estatística, incluindo correlações, distribuições e comparações de médias, permitiu identificar tendências e gaps educacionais, úteis para políticas públicas direcionadas.

Além disso, a transformação de dados (como raiz quadrada para normalização) foi essencial para melhorar a modelagem estatística, garantindo análises mais precisas.

Este estudo reforça a importância de avaliações em larga escala para monitorar a qualidade da educação e reduzir disparidades, contribuindo para um sistema educacional mais equitativo e eficiente.
""")
