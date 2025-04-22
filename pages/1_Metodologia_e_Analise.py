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
**Tamanho do arquivo depois:** 373.79 MB  
""")

st.markdown("""
**Presenças nas provas:**
- Faltaram Dia 1 e foram Dia 2: 11.356 (0.27%)  
- Foram Dia 1 e faltaram Dia 2: 254.521 (6.12%)  
- Faltaram nos dois dias: 1.354.127 (32.55%)
""")

# ========================
# Seção: 30 Questões
# ========================
st.header("❓ 30 Questões Respondidas")

questoes = [
    "Q1: Maior média em Matemática: MG",
    "Q2: Menor média em Redação: AM",
    "Q3: Sexo com maior média em Linguagens: Masculino",
    "Q4: Renda com maior média em CN: Mais de *R$* 19.080,00",
    "Q5: Média Matemática (com/sem internet): Com internet: 548.64 - Sem internet: 494.11",
    "Q6: Cor/Raça mais comum: Parda",
    "Q7: Tipo escola com maior nota Redação: Somente privada (sem bolsa)",
    "Q8: Faixa etária mais comum: 18 anos",
    "Q9: Cor/Raça com maior média CH: Branca",
    "Q10: Sexo com maior mediana em Redação: Feminino",
    "Q11: Maior correlação: Ciências Humanas e Linguagens",
    "Q12: Nota mais variável: Redação",
    "Q13: Renda mais comum entre top 10% Matemática: *R$* 954,01 a *R$* 1.431,00",
    "Q14: % Mulheres com redação > 800: 3.05%",
    "Q15: Estado com mais notas zero em CN: SP",
    "Q16: Idade média top 10% Matemática: 4.3",
    "Q17: Diferença média nota MT por sexo: 41.86",
    "Q18: Nota média Redação por internet: Com: 530.31 - Sem: 442.19",
    "Q19: % Escola pública: 76.33%",
    "Q20: Diferença nota Redação internet: 88.12",
    "Q21: Mediana Redação por raça: Amarela: 520 | Branca: 560 | Indígena: 420 | Parda: 500 | Preta: 480 | Não declarado: 540",
    "Q22: Maior desvio padrão em CH: PI",
    "Q23: Renda mais comum top 5% Redação: *R$* 954,01 a *R$* 1.431,00",
    "Q24: % notas 1000 Redação: 0.0010%",
    "Q25: Média MT por tipo de escola: Pública: 514.20 | Privada sem bolsa: 625.59",
    "Q26: Top 1% CN por sexo: Masc: 55.3% - Fem: 44.7%",
    "Q27: Faixa etária com maior média LC: Menor de 17 anos",
    "Q28: Estado com maior média em CN: DF",
    "Q29: Proporção nota 1000 Redação: Pública: 0.0001% | Privada: 0.0038%",
    "Q30: Estado com maior diferença pública x privada (MT): MG"
]

for q in questoes:
    st.markdown(f"- {q}")

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
