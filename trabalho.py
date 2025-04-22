import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# CONFIGURAÇÕES INICIAIS
# ==========================
st.set_page_config(page_title="Painel ENEM - Governo do Brasil", layout="wide")
st.title("📊 Painel Interativo ENEM - Governo Federal")
st.markdown("Este painel apresenta uma análise dos microdados do ENEM de forma interativa, acessível e informativa para a sociedade.")

# ==========================
# LEITURA DOS DADOS
# ==========================
@st.cache_data
def carregar_dados():
    return pd.read_csv("microdados_enem.csv", sep=",")

df = carregar_dados()

# ==========================
# RENOMEANDO PARA MAIOR CLAREZA
# ==========================
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

# ==========================
# FILTROS
# ==========================
st.sidebar.header("Filtros")
ufs = df["UF_Escola"].dropna().unique()
uf_sel = st.sidebar.selectbox("UF da Escola", options=sorted(ufs), index=0)

sexo_sel = st.sidebar.multiselect("Sexo", options=["F", "M"], default=["F", "M"])
cor_sel = st.sidebar.multiselect("Cor/Raça", options=sorted(df["Cor_Raca"].dropna().unique()), default=df["Cor_Raca"].dropna().unique())

df_filtros = df[
    (df["UF_Escola"] == uf_sel) &
    (df["Sexo"].isin(sexo_sel)) &
    (df["Cor_Raca"].isin(cor_sel))
]

# ==========================
# MÉDIA DAS NOTAS POR DISCIPLINA
# ==========================
st.markdown("## 🧮 Médias das Notas por Disciplina")
medias = df_filtros[["Nota_Ciencias_Natureza", "Nota_Ciencias_Humanas", "Nota_Linguagens", "Nota_Matematica", "Nota_Redacao"]].mean()
st.bar_chart(medias)

# ==========================
# DISTRIBUIÇÃO POR SEXO
# ==========================
st.markdown("## 📈 Distribuição de Notas por Sexo")
disciplina = st.selectbox("Selecione a disciplina:", [
    "Nota_Ciencias_Natureza", "Nota_Ciencias_Humanas",
    "Nota_Linguagens", "Nota_Matematica", "Nota_Redacao"
])

plt.figure(figsize=(10, 5))
sns.histplot(data=df_filtros, x=disciplina, hue="Sexo", kde=True, bins=30)
plt.title(f"Distribuição das Notas em {disciplina}", fontsize=16)
st.pyplot(plt.gcf())
plt.clf()

# ==========================
# GRÁFICO DE RENDA VS NOTA
# ==========================
st.markdown("## 💰 Renda Familiar e Desempenho")
renda_vs_nota = df_filtros.groupby("Renda_Familiar")[disciplina].mean().sort_values()
plt.figure(figsize=(10, 5))
renda_vs_nota.plot(kind='bar', color='green')
plt.title(f'Média de {disciplina} por Faixa de Renda Familiar')
plt.xlabel('Faixa de Renda (Q006)')
plt.ylabel('Nota Média')
st.pyplot(plt.gcf())
plt.clf()

# ==========================
# EXPLICAÇÕES E CÓDIGOS DE VARIÁVEIS
# ==========================
with st.expander("ℹ️ Sobre os Códigos das Variáveis"):
    st.markdown("""
    **TP_COR_RACA:**  
    0 - Não declarado  
    1 - Branca  
    2 - Preta  
    3 - Parda  
    4 - Amarela  
    5 - Indígena

    **Q006 - Renda Familiar:**  
    A - Nenhuma renda  
    B - Até R$ 998,00  
    C - De R$ 998,01 até R$ 1.497,00  
    ...  
    Q - Acima de R$ 9.600,01  
    """)
