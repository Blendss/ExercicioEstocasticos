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

st.header("💡 Perguntas respondidas com gráficos")
st.markdown("""
Acessando a página "respostas" no painel a esquerda, há 30 perguntas respondidas com gráficos estáticos e um dicionário para as legendas no topo da página
""")

st.header("📚 Conclusão: Análise Estatística dos Microdados do ENEM 2018")

# Introdução
st.markdown("""
## 1. Fluxo de trabalho
Esta análise exploratória dos microdados do ENEM 2018, com amostra de **660 mil participantes**, revelou padrões educacionais significativos através de técnicas de análise exploratória de dados, estatísticas descritivas e inferenciais. Realizou-se:
- **Remoção de colunas indesejadas**
- **Limpesa de dados**
- **Conversão para arquivo menor**
- **Criação de gráficos interativos e estáticos**
- **Conclusão feita com as informações**
""")

# Seção 1 - Principais Resultados
with st.container():
    st.header("2. Principais Resultados Obtidos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔎 Desigualdades Regionais")
        st.markdown("""
        - **MG** destacou-se com a **maior média em Matemática (558,51 pontos)**, enquanto **RR** apresentou a **menor performance em Redação (460,43 pontos)**
        - **DF** liderou em Ciências da Natureza (509,56), contrastando com **AC** (466,1), evidenciando:
          * Disparidades na formação docente regional
          * Diferenças na infraestrutura escolar
          * Variações curriculares estaduais
        """)
        
    with col2:
        st.subheader("📉 Impacto Socioeconômico")
        st.markdown("""
        - Estudantes de **escolas privadas** tiveram desempenho superior:
          * **+155,51 pontos** em Matemática
          * **+165,18 pontos** em Redação
        - A **renda familiar** mostrou correlação positiva (r = 0,68) com o desempenho
        - O **acesso à internet** influenciou em:
          * **+54,55 pontos** em Matemática
          * **+88,46 pontos** em Redação
        """)

# Seção 2 - Análises Detalhadas
st.header("3. Análises Específicas por Variável")

with st.expander("👥 Variáveis Demográficas"):
    st.markdown("""
    ### 3.1 Gênero
    - **Homens** apresentaram melhor desempenho em:
      * Linguagens (532,62 vs 510,45; p < 0,01)
      * Matemática (diferença de 42,31 pontos)
    - **Mulheres** tiveram maior mediana em Redação (520,0 vs 480,0)
    - No top 1% de Ciências da Natureza: 57,5% homens vs 42,5% mulheres
    
    ### 3.2 Cor/Raça
    - **Brancos** lideraram em Ciências Humanas (589,73)
    - **Pardos** foram maioria (303.620 participantes)
    - **Indígenas** tiveram menor mediana em Redação (420,0)
    - Disparidade máxima: 140 pontos entre grupos extremos
    """)

with st.expander("📊 Análise de Distribuições"):
    st.markdown("""
    ### 3.3 Normalidade das Variáveis
    - Transformação por **raiz quadrada** mostrou melhor ajuste que log(1+y)
    - QQ-plots revelaram:
      * Caudas pesadas na distribuição original
      * Melhor simetria após transformação
    
    ### 3.4 Variabilidade
    - **Redação** apresentou maior variabilidade (DP = 184,44)
    - **PI** teve maior desvio padrão em CH (83,60)
    - Coeficiente de variação:
      * Redação: 34,2%
      * Matemática: 18,7%
    """)

# Seção 3 - Limitações e Recomendações
st.header("4. Limitações e Propostas de Intervenção")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚠️ Limitações do Estudo")
    st.markdown("""
    - Dados auto-declaratórios podem conter viés
    - Amostra não probabilística
    - Variáveis omitidas (ex.: qualidade docente)
    - Restrição a participantes presentes em todas as provas
    """)

with col2:
    st.subheader("💡 Recomendações")
    st.markdown("""
    - **Políticas públicas focalizadas** em estados com baixo desempenho
    - **Programas de inclusão digital** para reduzir gap tecnológico
    - **Capacitação docente** em regiões periféricas
    - **Ações afirmativas** para grupos com menor desempenho médio
    - **Estudos longitudinais** para avaliar tendências
    """)

# Considerações Finais
st.header("5. Conclusões Finais")
st.markdown("""
Esta análise estatística revelou **padrões estruturais de desigualdade educacional** no Brasil, onde:

1. **Fatores socioeconômicos** (renda, tipo de escola) explicam grande parte da variância no desempenho  
2. **Variáveis regionais** apresentam diferenças estatisticamente significativas  
3. **Gênero e raça** influenciam padrões de desempenho específicos  

Os resultados demonstram como características extra-escolares impactam o desempenho acadêmico. A transformação de dados mostrou-se essencial para análises inferenciais válidas. 
""")

# Rodapé
st.divider()
st.caption("""
Trabalho realizado para a disciplina Processos Estocásticos - UNISO  
Autores: Thomas Buchser Monteiro - 2025  
Dados: INEP/MEC - Microdados ENEM 2018  
Metodologia: Análise Exploratória, Estatística Descritiva e Inferencial
""")
