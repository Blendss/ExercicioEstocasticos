import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# ==========================
# CONFIGURAÇÕES INICIAIS
# ==========================
st.set_page_config(page_title="Painel ENEM - Governo do Brasil", layout="wide")
st.title("📊 Painel Interativo ENEM - Governo Federal")
st.markdown(
    "Este painel apresenta uma análise dos microdados do ENEM de forma interativa, acessível e informativa para a sociedade.",
)

# ==========================
# LEITURA DOS DADOS
# ==========================
@st.cache_data
def carregar_dados():
    df = pd.read_csv("microdados_enem.csv", sep=",")
    df.rename(columns={
        "TP_SEXO": "Sexo",
        "TP_COR_RACA": "Cor_Raca",
        "SG_UF_ESC": "UF_Escola",
        "NU_NOTA_CN": "Nota_Ciencias_Natureza",
        "NU_NOTA_CH": "Nota_Ciencias_Humanas",
        "NU_NOTA_LC": "Nota_Linguagens",
        "NU_NOTA_MT": "Nota_Matematica",
        "NU_NOTA_REDACAO": "Nota_Redacao",
        "Q006": "Renda_Familiar"
    }, inplace=True)
    return df

df = carregar_dados()

# ==========================
# SIDEBAR DE FILTROS
# ==========================
st.sidebar.header("Filtros")
ufs = df["UF_Escola"].dropna().unique()
uf_sel = st.sidebar.selectbox("UF da Escola", options=sorted(ufs), index=0)
sexo_sel = st.sidebar.multiselect("Sexo", options=["F", "M"], default=["F", "M"])
cor_sel = st.sidebar.multiselect(
    "Cor/Raça", options=sorted(df["Cor_Raca"].dropna().unique()),
    default=df["Cor_Raca"].dropna().unique()
)
renda_sel = st.sidebar.multiselect(
    "Faixa de Renda Familiar", options=sorted(df["Renda_Familiar"].dropna().unique()),
    default=sorted(df["Renda_Familiar"].dropna().unique())
)

df_filtrado = df[
    (df["UF_Escola"] == uf_sel) &
    (df["Sexo"].isin(sexo_sel)) &
    (df["Cor_Raca"].isin(cor_sel)) &
    (df["Renda_Familiar"].isin(renda_sel))
]

with st.expander("ℹ️ Sobre os Códigos das Variáveis"):
    st.markdown("""
        **TP_COR_RACA:** 0-Não declarado, 1-Branca, 2-Preta, 3-Parda, 4-Amarela, 5-Indígena

        **Q006 - Renda Familiar:**
        - A: Nenhuma renda
        - B: Até *R$* 998,00
        - C: De *R$* 998,01 até *R$* 1.497,00
        - D: De *R$* 1.431,01 até *R$* 1.908,00.
        - E: De *R$* 1.908,01 até *R$* 2.385,00.
        - F: De *R$* 2.385,01 até *R$* 2.862,00.
        - G: De *R$* 2.862,01 até *R$* 3.816,00.
        - H: De *R$* 3.816,01 até *R$* 4.770,00.
        - I: De *R$* 4.770,01 até *R$* 5.724,00.
        - J: De *R$* 5.724,01 até *R$* 6.678,00.
        - K: De *R$* 6.678,01 até *R$* 7.632,00.
        - L: De *R$* 7.632,01 até *R$* 8.586,00.
        - M: De *R$* 8.586,01 até *R$* 9.540,00.
        - N: De *R$* 9.540,01 até *R$* 11.448,00.
        - O: De *R$* 11.448,01 até *R$* 14.310,00.
        - P: De *R$* 14.310,01 até *R$* 19.080,00.
        - Q: Acima de *R$* 9.600,01
    """)

# ==========================
# GRÁFICO 1: Disparidade de Nota por Renda (Boxplot)
# ==========================
st.markdown("## 💰 Disparidade de Notas por Faixa de Renda")
materia_1 = st.selectbox(
    "Matéria para o gráfico de renda:", 
    options=[
        "Nota_Matematica", "Nota_Linguagens", "Nota_Ciencias_Humanas", 
        "Nota_Ciencias_Natureza", "Nota_Redacao"
    ],
    format_func=lambda x: x.replace("Nota_", "").replace("_", " "),
    key="materia_boxplot"
)
plt.figure(figsize=(10, 5))
sns.boxplot(
    data=df_filtrado,
    x="Renda_Familiar",
    y=materia_1,
    order=sorted(df_filtrado["Renda_Familiar"].unique())
)
plt.xticks(rotation=45)
plt.xlabel("Faixa de Renda Familiar")
plt.ylabel(f"{materia_1.replace('Nota_', '').replace('_', ' ')}")
plt.title(f"Distribuição das Notas de {materia_1.replace('Nota_', '').replace('_', ' ')} por Faixa de Renda")
st.pyplot(plt.gcf())
plt.clf()

st.markdown(
    "**Análise:** Observa-se que, em média, alunos de faixas de renda mais altas tendem a obter notas superiores. "
    "Essa disparidade evidencia desafios de acesso a recursos educacionais e desigualdade socioeconômica."
)

# ==========================
# GRÁFICO 2: Renda vs Redação (Scatter interativo Altair)
# ==========================
st.markdown("## 📈 Renda Familiar vs Nota por Participante")
materia_2 = st.selectbox(
    "Matéria para o gráfico de dispersão:", 
    options=[
        "Nota_Matematica", "Nota_Linguagens", "Nota_Ciencias_Humanas", 
        "Nota_Ciencias_Natureza", "Nota_Redacao"
    ],
    format_func=lambda x: x.replace("Nota_", "").replace("_", " "),
    key="materia_scatter"
)
select = alt.selection_interval(encodings=['x', 'y'])
chart = alt.Chart(df_filtrado).mark_circle(size=60).encode(
    x=alt.X('Renda_Familiar:N', title='Faixa de Renda'),
    y=alt.Y(f'{materia_2}:Q', title=f'Nota de {materia_2.replace("Nota_", "").replace("_", " ")}'),
    color='Cor_Raca:N',
    tooltip=['Sexo', 'Cor_Raca', materia_2, 'Renda_Familiar']
).properties(width=700, height=400).add_selection(select)
st.altair_chart(chart, use_container_width=True)

st.markdown(
    "**Análise:** Cada ponto representa um participante do ENEM. "
    "A tendência mostra que faixas de renda mais elevadas concentram notas maiores, "
    "sugerindo influência de suporte e recursos externos na preparação."
)

# ==========================
# GRÁFICO 3: Notas por Cor/Raça (Violin plot)
# ==========================
st.markdown("## 🎨 Distribuição de Notas por Cor/Raça")
materia_3 = st.selectbox(
    "Matéria para o gráfico de violino:", 
    options=[
        "Nota_Matematica", "Nota_Linguagens", "Nota_Ciencias_Humanas", 
        "Nota_Ciencias_Natureza", "Nota_Redacao"
    ],
    format_func=lambda x: x.replace("Nota_", "").replace("_", " "),
    key="materia_violin"
)
plt.figure(figsize=(10,5))
sns.violinplot(
    data=df_filtrado,
    x="Cor_Raca",
    y=materia_3,
    order=sorted(df_filtrado["Cor_Raca"].unique())
)
plt.xlabel("Cor/Raça")
plt.ylabel(materia_3.replace("Nota_", "").replace("_", " "))
plt.title(f"Distribuição de Notas de {materia_3.replace('Nota_', '').replace('_', ' ')} por Cor/Raça")
st.pyplot(plt.gcf())
plt.clf()

st.markdown(
    "**Análise:** As diferenças nas distribuições indicam que estudantes autodeclarados pretos e pardos enfrentam maiores desafios, "
    "possivelmente refletindo desigualdades históricas no acesso a uma educação de qualidade."
)

# ==========================
# GRÁFICO 4: Média de Notas por Estado com Seletor de Matéria
# ==========================
st.markdown("## 📍 Média das Notas por UF")
materia_4 = st.selectbox(
    "Matéria para o gráfico de médias por estado:", 
    options=[
        "Nota_Matematica", "Nota_Linguagens", "Nota_Ciencias_Humanas", 
        "Nota_Ciencias_Natureza", "Nota_Redacao"
    ],
    format_func=lambda x: x.replace("Nota_", "").replace("_", " "),
    key="materia_uf"
)

media_uf = (
    df_filtrado.groupby('UF_Escola')[materia_4]
    .mean()
    .reset_index()
    .rename(columns={materia_4: 'Media_Nota'})
)

chart_uf = alt.Chart(media_uf).mark_bar().encode(
    x=alt.X('UF_Escola:N', sort='-y'),
    y=alt.Y('Media_Nota:Q', title=f'Média - {materia_4.replace("Nota_", "").replace("_", " ")}'),
    tooltip=['UF_Escola', 'Media_Nota']
).properties(width=700, height=400)

st.altair_chart(chart_uf, use_container_width=True)

st.markdown(f"""
**Análise:** Este gráfico mostra a média da disciplina **{materia_4.replace("Nota_", "").replace("_", " ")}** por estado.  
As diferenças entre UFs evidenciam desigualdades regionais, que podem estar ligadas a fatores como infraestrutura escolar, formação de professores, acesso a recursos e políticas educacionais locais.  
Ao identificar estados com desempenho mais baixo, é possível orientar ações específicas de investimento e melhoria.  
""")
