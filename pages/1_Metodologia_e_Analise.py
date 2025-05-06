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
A análise estatística dos microdados do ENEM 2018 permitiu observar importantes 
padrões e desigualdades no desempenho dos participantes em diferentes áreas do 
conhecimento, considerando variáveis socioeconômicas, demográficas e 
educacionais. Utilizando técnicas exploratórias e de correlação, foi possível identificar 
relações significativas e até esperadas, como a maior média de matemática no estado 
de Minas Gerais (Q1) e a menor média em redação no Amazonas (Q2), refletindo 
possíveis desigualdades regionais. 
Além disso, destacam-se diferenças de desempenho por sexo (Q3, Q10, Q17), cor/raça 
(Q6, Q9, Q21), tipo de escola (Q7, Q25, Q29, Q30), renda familiar (Q4, Q13, Q23), e 
acesso à internet (Q5, Q18, Q20), que reforçam o impacto do contexto 
socioeconômico na performance dos candidatos. 
As análises também evidenciaram que a nota com maior variabilidade é a de redação 
(Q12), o que pode indicar um maior componente subjetivo na avaliação, e que a maior 
correlação entre notas foi entre Ciências Humanas e Linguagens (Q11 e matriz de 
correlação), o que pode apontar para perfis cognitivos semelhantes. 
Para a modelagem estatística dos dados e avaliação de normalidade das variáveis, 
especialmente a nota de redação, foi aplicada a transformação do tipo log(1 + y) e 
posteriormente comparada com a transformação por raiz quadrada. Concluímos que a 
raiz quadrada apresentou melhor desempenho na simetrização da distribuição, 
resultando em gráficos QQ mais alinhados com a normalidade teórica — o que é 
desejável em muitos modelos probabilísticos, como regressões lineares e análise de 
componentes principais. 
Esses resultados reforçam a importância da análise estatística aplicada a grandes 
volumes de dados educacionais, como forma de revelar desigualdades, orientar 
políticas públicas e aprimorar modelos preditivos. Técnicas de Processos 
Estocásticos, em especial, se mostram úteis ao estudar a distribuição e variabilidade 
das notas, bem como para modelar o comportamento dos candidatos frente a fatores 
externos.
""")
