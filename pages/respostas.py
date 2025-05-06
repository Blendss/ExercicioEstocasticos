import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import numpy as np

# Configurações iniciais
st.set_page_config(page_title="Análise ENEM 2018 - 30 Questões", layout="wide")
st.title("📊 Análise ENEM 2018 - 30 Questões Respondidas com Visualizações")
st.header("amostra de 660 mil estudantes")

# Leitura dos dados
@st.cache_data
def carregar_dados():
    df = pd.read_parquet("amostra_presentes_max25mb.parquet", engine='fastparquet')
    df.rename(columns={
        "TP_SEXO": "Sexo",
        "TP_COR_RACA": "Cor_Raca",
        "SG_UF_ESC": "UF_Escola",
        "NU_NOTA_CN": "Nota_Ciencias_Natureza",
        "NU_NOTA_CH": "Nota_Ciencias_Humanas",
        "NU_NOTA_LC": "Nota_Linguagens",
        "NU_NOTA_MT": "Nota_Matematica",
        "NU_NOTA_REDACAO": "Nota_Redacao",
        "Q006": "Renda_Familiar",
        "Q025": "Internet_Domicilio"
    }, inplace=True)
    return df

df = carregar_dados()

with st.expander("ℹ️ Sobre os Códigos das Variáveis"):
    st.markdown("""
        **TP_COR_RACA:** 0-Não declarado, 1-Branca, 2-Preta, 3-Parda, 4-Amarela, 5-Indígena

        **IN_TREINEIRO** 0-Nâo treineiro 1-Treineiro

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


# =============================================
# Q1: Maior média em Matemática
# =============================================
media_mt_uf = df.groupby('UF_Escola')['Nota_Matematica'].mean().sort_values(ascending=False).reset_index()
maior_media_mt_uf = media_mt_uf.iloc[0]['UF_Escola']
maior_media_mt_valor = media_mt_uf.iloc[0]['Nota_Matematica']

st.header(f"Q1: Maior média em Matemática: {maior_media_mt_uf}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_mt_uf, x='UF_Escola', y='Nota_Matematica', palette='viridis')
plt.title('Média de Matemática por Estado')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com maior média em Matemática é {maior_media_mt_uf} com {maior_media_mt_valor:.2f} pontos.
""")

# =============================================
# Q2: Menor média em Redação
# =============================================
media_redacao_uf = df.groupby('UF_Escola')['Nota_Redacao'].mean().sort_values().reset_index()
menor_media_redacao_uf = media_redacao_uf.iloc[0]['UF_Escola']
menor_media_redacao_valor = media_redacao_uf.iloc[0]['Nota_Redacao']

st.header(f"Q2: Menor média em Redação: {menor_media_redacao_uf}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_redacao_uf, x='UF_Escola', y='Nota_Redacao', palette='viridis')
plt.title('Média de Redação por Estado')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com menor média em Redação é {menor_media_redacao_uf} com {menor_media_redacao_valor:.2f} pontos.
""")

# =============================================
# Q3: Sexo com maior média em Linguagens
# =============================================
media_lc_sexo = df.groupby('Sexo')['Nota_Linguagens'].mean().sort_values(ascending=False).reset_index()
sexo_maior_media_lc = media_lc_sexo.iloc[0]['Sexo']
maior_media_lc_valor = media_lc_sexo.iloc[0]['Nota_Linguagens']

st.header(f"Q3: Sexo com maior média em Linguagens: {sexo_maior_media_lc}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_lc_sexo, x='Sexo', y='Nota_Linguagens', palette='coolwarm')
plt.title('Média de Linguagens por Sexo')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O sexo com maior média em Linguagens é {sexo_maior_media_lc} com {maior_media_lc_valor:.2f} pontos.
""")

# =============================================
# Q4: Renda com maior média em CN
# =============================================
media_cn_renda = df.groupby('Renda_Familiar')['Nota_Ciencias_Natureza'].mean().sort_values(ascending=False).reset_index()
renda_maior_media_cn = media_cn_renda.iloc[0]['Renda_Familiar']
maior_media_cn_valor = media_cn_renda.iloc[0]['Nota_Ciencias_Natureza']

st.header(f"Q4: Renda com maior média em CN: {renda_maior_media_cn}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_cn_renda, x='Renda_Familiar', y='Nota_Ciencias_Natureza', palette='viridis')
plt.title('Média de Ciências da Natureza por Faixa de Renda')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A faixa de renda com maior média em Ciências da Natureza é '{renda_maior_media_cn}' com {maior_media_cn_valor:.2f} pontos.
""")

# =============================================
# Q5: Média Matemática (com/sem internet)
# =============================================
media_mt_internet = df.groupby('Internet_Domicilio')['Nota_Matematica'].mean().reset_index()
media_mt_internet['Internet_Domicilio'] = media_mt_internet['Internet_Domicilio'].map({'A': 'Sem internet', 'B': 'Com internet'})
media_com_internet = media_mt_internet[media_mt_internet['Internet_Domicilio'] == 'Com internet']['Nota_Matematica'].values[0]
media_sem_internet = media_mt_internet[media_mt_internet['Internet_Domicilio'] == 'Sem internet']['Nota_Matematica'].values[0]
diferenca_internet = media_com_internet - media_sem_internet

st.header("Q5: Média Matemática (com/sem internet)")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_mt_internet, x='Internet_Domicilio', y='Nota_Matematica', palette='Set2')
plt.title('Média de Matemática por Acesso à Internet')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** 
- Com internet: {media_com_internet:.2f}
- Sem internet: {media_sem_internet:.2f}
- Diferença: {diferenca_internet:.2f} pontos
""")

# =============================================
# Q6: Cor/Raça mais comum
# =============================================
cor_raca_counts = df['Cor_Raca'].value_counts().reset_index()
cor_raca_counts.columns = ['Cor_Raca', 'Count']
cor_raca_counts['Cor_Raca'] = cor_raca_counts['Cor_Raca'].map({
    0: 'Não declarado', 1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena'
})
cor_raca_mais_comum = cor_raca_counts.iloc[0]['Cor_Raca']
count_cor_raca = cor_raca_counts.iloc[0]['Count']

st.header(f"Q6: Cor/Raça mais comum: {cor_raca_mais_comum}")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=cor_raca_counts, x='Cor_Raca', y='Count', palette='Set3')
plt.title('Distribuição de Participantes por Cor/Raça')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A cor/raça mais comum entre os participantes é '{cor_raca_mais_comum}' com {count_cor_raca:,} participantes.
""")

# =============================================
# Q7: Tipo escola com maior nota Redação
# =============================================
media_redacao_escola = df.groupby('TP_ESCOLA')['Nota_Redacao'].mean().sort_values(ascending=False).reset_index()
media_redacao_escola['TP_ESCOLA'] = media_redacao_escola['TP_ESCOLA'].map({
    1: 'Não Respondeu', 2: 'Pública', 3: 'Exterior', 4: 'Privada'
})
tipo_escola_maior_redacao = media_redacao_escola.iloc[0]['TP_ESCOLA']
media_maior_redacao = media_redacao_escola.iloc[0]['Nota_Redacao']

st.header(f"Q7: Tipo escola com maior nota Redação: {tipo_escola_maior_redacao}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_redacao_escola, x='TP_ESCOLA', y='Nota_Redacao', palette='Set2')
plt.title('Média de Redação por Tipo de Escola')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O tipo de escola com maior média em Redação é '{tipo_escola_maior_redacao}' com {media_maior_redacao:.2f} pontos.
""")

# =============================================
# Q8: Faixa etária mais comum
# =============================================
faixa_etaria_map = {
    1: 'Menor de 17 anos',
    2: '17 anos',
    3: '18 anos',
    4: '19 anos',
    5: '20 anos',
    6: '21 anos',
    7: '22 anos',
    8: '23 anos',
    9: '24 anos',
    10: '25 anos',
    11: 'Entre 26 e 30 anos',
    12: 'Entre 31 e 35 anos',
    13: 'Entre 36 e 40 anos',
    14: 'Entre 41 e 45 anos',
    15: 'Entre 46 e 50 anos',
    16: 'Entre 51 e 55 anos',
    17: 'Entre 56 e 60 anos',
    18: 'Entre 61 e 65 anos',
    19: 'Entre 66 e 70 anos',
    20: 'Maior de 70 anos'
}

idade_counts = df['TP_FAIXA_ETARIA'].value_counts().reset_index()
idade_counts.columns = ['Codigo_Faixa', 'Count']
idade_counts['Faixa_Etaria'] = idade_counts['Codigo_Faixa'].map(faixa_etaria_map)
faixa_etaria_mais_comum = idade_counts.iloc[0]['Faixa_Etaria']
count_faixa_etaria = idade_counts.iloc[0]['Count']

st.header(f"Q8: Faixa etária mais comum: {faixa_etaria_mais_comum}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=idade_counts.head(10), x='Faixa_Etaria', y='Count', palette='viridis')
plt.title('Distribuição de Participantes por Faixa Etária (Top 10)')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A faixa etária mais comum entre os participantes é '{faixa_etaria_mais_comum}' com {count_faixa_etaria:,} participantes.
""")

# =============================================
# Q9: Cor/Raça com maior média CH
# =============================================
media_ch_raca = df.groupby('Cor_Raca')['Nota_Ciencias_Humanas'].mean().sort_values(ascending=False).reset_index()
media_ch_raca['Cor_Raca'] = media_ch_raca['Cor_Raca'].map({
    0: 'Não declarado', 1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena'
})
cor_raca_maior_ch = media_ch_raca.iloc[0]['Cor_Raca']
media_maior_ch = media_ch_raca.iloc[0]['Nota_Ciencias_Humanas']

st.header(f"Q9: Cor/Raça com maior média CH: {cor_raca_maior_ch}")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=media_ch_raca, x='Cor_Raca', y='Nota_Ciencias_Humanas', palette='Set3')
plt.title('Média de Ciências Humanas por Cor/Raça')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A cor/raça com maior média em Ciências Humanas é '{cor_raca_maior_ch}' com {media_maior_ch:.2f} pontos.
""")

# =============================================
# Q10: Sexo com maior mediana em Redação
# =============================================
mediana_redacao_sexo = df.groupby('Sexo')['Nota_Redacao'].median().sort_values(ascending=False).reset_index()
sexo_maior_mediana = mediana_redacao_sexo.iloc[0]['Sexo']
maior_mediana_valor = mediana_redacao_sexo.iloc[0]['Nota_Redacao']

st.header(f"Q10: Sexo com maior mediana em Redação: {sexo_maior_mediana}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=mediana_redacao_sexo, x='Sexo', y='Nota_Redacao', palette='coolwarm')
plt.title('Mediana de Redação por Sexo')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O sexo com maior mediana em Redação é '{sexo_maior_mediana}' com {maior_mediana_valor:.2f} pontos.
""")

# =============================================
# Q11: Maior correlação entre notas
# =============================================
correlacoes = df[['Nota_Ciencias_Humanas', 'Nota_Linguagens', 'Nota_Matematica', 'Nota_Ciencias_Natureza', 'Nota_Redacao']].corr()
max_corr = correlacoes.unstack().sort_values(ascending=False)
max_corr = max_corr[max_corr < 1].head(1)
materia1 = max_corr.index[0][0].replace("Nota_", "").replace("_", " ")
materia2 = max_corr.index[0][1].replace("Nota_", "").replace("_", " ")
valor_correlacao = max_corr.values[0]

st.header(f"Q11: Maior correlação: {materia1} e {materia2}")

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação entre as Notas')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A maior correlação é entre {materia1} e {materia2} com {valor_correlacao:.3f}.
""")

# =============================================
# Q12: Nota mais variável
# =============================================
desvios_padrao = df[['Nota_Ciencias_Humanas', 'Nota_Linguagens', 'Nota_Matematica', 'Nota_Ciencias_Natureza', 'Nota_Redacao']].std().sort_values(ascending=False).reset_index()
desvios_padrao.columns = ['Matéria', 'Desvio_Padrão']
materia_mais_variavel = desvios_padrao.iloc[0]['Matéria'].replace("Nota_", "").replace("_", " ")
desvio_padrao_valor = desvios_padrao.iloc[0]['Desvio_Padrão']

st.header(f"Q12: Nota mais variável: {materia_mais_variavel}")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=desvios_padrao, x='Matéria', y='Desvio_Padrão', palette='viridis')
plt.title('Desvio Padrão das Notas por Matéria')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A nota mais variável é '{materia_mais_variavel}' com desvio padrão de {desvio_padrao_valor:.2f}.
""")

# =============================================
# Q13: Renda mais comum entre top 10% Matemática
# =============================================
top_10_mt = df.nlargest(int(len(df)*0.1), 'Nota_Matematica')
renda_top10_counts = top_10_mt['Renda_Familiar'].value_counts().reset_index()
renda_top10_counts.columns = ['Renda_Familiar', 'Count']
renda_mais_comum_top10 = renda_top10_counts.iloc[0]['Renda_Familiar']
count_renda_top10 = renda_top10_counts.iloc[0]['Count']

st.header(f"Q13: Renda mais comum entre top 10% Matemática: {renda_mais_comum_top10}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=renda_top10_counts, x='Renda_Familiar', y='Count', palette='viridis')
plt.title('Distribuição de Renda entre Top 10% em Matemática')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A renda mais comum entre o top 10% em Matemática é '{renda_mais_comum_top10}' com {count_renda_top10:,} participantes.
""")

# =============================================
# Q14: % Mulheres com redação > 800
# =============================================
mulheres = df[df['Sexo'] == 'F']
total_mulheres = len(mulheres)
mulheres_redacao_800 = len(mulheres[mulheres['Nota_Redacao'] > 800])
percentual_mulheres_800 = (mulheres_redacao_800 / total_mulheres) * 100

st.header(f"Q14: % Mulheres com redação > 800: {percentual_mulheres_800:.2f}%")

fig, ax = plt.subplots(figsize=(8, 5))
plt.pie([percentual_mulheres_800, 100-percentual_mulheres_800], labels=['> 800', '≤ 800'], autopct='%1.2f%%', colors=['#ff9999','#66b3ff'])
plt.title('Distribuição de Mulheres por Nota em Redação (>800)')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O percentual de mulheres com nota em Redação acima de 800 é {percentual_mulheres_800:.2f}%.
""")

# =============================================
# Q15: Estado com menor desempenho em Ciências da Natureza
# =============================================
media_cn_uf = df.groupby('UF_Escola')['Nota_Ciencias_Natureza'].mean().sort_values().reset_index()
uf_menor_cn = media_cn_uf.iloc[0]['UF_Escola']
media_menor_cn = media_cn_uf.iloc[0]['Nota_Ciencias_Natureza']
media_nacional_cn = df['Nota_Ciencias_Natureza'].mean()

st.header(f"Q15: Estado com menor desempenho em Ciências da Natureza: {uf_menor_cn}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_cn_uf, x='UF_Escola', y='Nota_Ciencias_Natureza', palette='viridis')
plt.axhline(y=media_nacional_cn, color='red', linestyle='--', label=f'Média Nacional: {media_nacional_cn:.1f}')
plt.title('Desempenho Médio em Ciências da Natureza por Estado')
plt.xlabel('Estado')
plt.ylabel('Média de Notas')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com menor desempenho médio em Ciências da Natureza é **{uf_menor_cn}** com média de {media_menor_cn:.1f} pontos, 
enquanto a média nacional é de {media_nacional_cn:.1f} pontos.
""")

# =============================================
# Q16: Faixa etária mais comum top 10% Matemática
# =============================================
top_10_mt = df.nlargest(int(len(df)*0.1), 'Nota_Matematica')
top_10_mt['Faixa_Etaria_Desc'] = top_10_mt['TP_FAIXA_ETARIA'].map(faixa_etaria_map)
faixa_counts = top_10_mt['Faixa_Etaria_Desc'].value_counts().reset_index()
faixa_counts.columns = ['Faixa_Etaria', 'Count']
faixa_mais_comum_top10 = faixa_counts.iloc[0]['Faixa_Etaria']
count_faixa_top10 = faixa_counts.iloc[0]['Count']

st.header(f"Q16: Faixa etária mais comum top 10% Matemática: {faixa_mais_comum_top10}")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=faixa_counts, x='Faixa_Etaria', y='Count', palette='viridis', order=faixa_counts['Faixa_Etaria'])
plt.title('Distribuição por Faixa Etária no Top 10% em Matemática')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A faixa etária mais comum no top 10% em Matemática é '{faixa_mais_comum_top10}' com {count_faixa_top10:,} participantes.
""")

# =============================================
# Q17: Diferença média nota MT por sexo
# =============================================
media_mt_sexo = df.groupby('Sexo')['Nota_Matematica'].mean().reset_index()
diferenca_mt_sexo = abs(media_mt_sexo.iloc[0]['Nota_Matematica'] - media_mt_sexo.iloc[1]['Nota_Matematica'])

st.header(f"Q17: Diferença média nota MT por sexo: {diferenca_mt_sexo:.2f}")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_mt_sexo, x='Sexo', y='Nota_Matematica', palette='coolwarm')
plt.title('Média de Matemática por Sexo')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A diferença de média em Matemática entre sexos é de {diferenca_mt_sexo:.2f} pontos.
""")

# =============================================
# Q18: Nota média Redação por internet
# =============================================
media_redacao_internet = df.groupby('Internet_Domicilio')['Nota_Redacao'].mean().reset_index()
media_redacao_internet['Internet_Domicilio'] = media_redacao_internet['Internet_Domicilio'].map({'A': 'Sem internet', 'B': 'Com internet'})
media_com_internet_red = media_redacao_internet[media_redacao_internet['Internet_Domicilio'] == 'Com internet']['Nota_Redacao'].values[0]
media_sem_internet_red = media_redacao_internet[media_redacao_internet['Internet_Domicilio'] == 'Sem internet']['Nota_Redacao'].values[0]
diferenca_internet_red = media_com_internet_red - media_sem_internet_red

st.header("Q18: Nota média Redação por internet")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_redacao_internet, x='Internet_Domicilio', y='Nota_Redacao', palette='Set2')
plt.title('Média de Redação por Acesso à Internet')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** 
- Com internet: {media_com_internet_red:.2f}
- Sem internet: {media_sem_internet_red:.2f}
- Diferença: {diferenca_internet_red:.2f} pontos
""")

# =============================================
# Q19: % Escola pública
# =============================================
total = len(df)
escola_publica = len(df[df['TP_ESCOLA'] == 2])
percentual_publica = (escola_publica / total) * 100

st.header(f"Q19: % Escola pública: {percentual_publica:.2f}%")

fig, ax = plt.subplots(figsize=(8, 5))
plt.pie([percentual_publica, 100-percentual_publica], labels=['Pública', 'Outras'], autopct='%1.2f%%', colors=['#66b3ff','#ff9999'])
plt.title('Proporção de Alunos de Escola Pública')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O percentual de alunos de escola pública é {percentual_publica:.2f}%.
""")

# =============================================
# Q20: Como a escolaridade dos pais afeta a nota de redação?
# =============================================
escolaridade_map = {
    'A': 'Nunca estudou',
    'B': 'Fundamental (1º-5º) incompleto',
    'C': 'Fundamental (1º-5º) completo',
    'D': 'Fundamental (6º-9º) completo',
    'E': 'Ensino Médio completo',
    'F': 'Superior completo',
    'G': 'Pós-graduação completa',
    'H': 'Não sabe'
}

df['Escolaridade_Pai'] = df['Q001'].map(escolaridade_map)
df['Escolaridade_Mae'] = df['Q002'].map(escolaridade_map)

ordem_escolaridade = [
    'Nunca estudou',
    'Fundamental (1º-5º) incompleto',
    'Fundamental (1º-5º) completo',
    'Fundamental (6º-9º) completo',
    'Ensino Médio completo',
    'Superior completo',
    'Pós-graduação completa',
    'Não sabe'
]

media_redacao_pai = df.groupby('Escolaridade_Pai')['Nota_Redacao'].mean().reindex(ordem_escolaridade).reset_index()
media_redacao_mae = df.groupby('Escolaridade_Mae')['Nota_Redacao'].mean().reindex(ordem_escolaridade).reset_index()

st.header("Q20: Como a escolaridade dos pais afeta a nota de redação?")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

sns.barplot(data=media_redacao_pai, x='Escolaridade_Pai', y='Nota_Redacao', 
            ax=ax1, palette='Blues_d', order=ordem_escolaridade)
ax1.set_title('Média de Redação por Escolaridade do Pai', pad=20)
ax1.set_xlabel('Nível de Escolaridade', labelpad=10)
ax1.set_ylabel('Média da Nota de Redação', labelpad=10)
ax1.tick_params(axis='x', rotation=55)

sns.barplot(data=media_redacao_mae, x='Escolaridade_Mae', y='Nota_Redacao', 
            ax=ax2, palette='Oranges_d', order=ordem_escolaridade)
ax2.set_title('Média de Redação por Escolaridade da Mãe', pad=20)
ax2.set_xlabel('Nível de Escolaridade', labelpad=10)
ax2.set_ylabel('')
ax2.tick_params(axis='x', rotation=55)

plt.tight_layout()
st.pyplot(fig)

dados_validos_pai = media_redacao_pai[media_redacao_pai['Escolaridade_Pai'] != 'Não sabe']
dados_validos_mae = media_redacao_mae[media_redacao_mae['Escolaridade_Mae'] != 'Não sabe']

diferenca_pai = dados_validos_pai['Nota_Redacao'].max() - dados_validos_pai['Nota_Redacao'].min()
diferenca_mae = dados_validos_mae['Nota_Redacao'].max() - dados_validos_mae['Nota_Redacao'].min()

st.markdown(f"""
**Resposta confirmada:**
- Diferença entre extremos (pai): {diferenca_pai:.1f} pontos
- Diferença entre extremos (mãe): {diferenca_mae:.1f} pontos
- Impacto médio por nível educacional: {(diferenca_mae/7):.1f} pontos
""")

# =============================================
# Q21: Mediana Redação por raça
# =============================================
mediana_redacao_raca = df.groupby('Cor_Raca')['Nota_Redacao'].median().sort_values(ascending=False).reset_index()
mediana_redacao_raca['Cor_Raca'] = mediana_redacao_raca['Cor_Raca'].map({
    0: 'Não declarado', 1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena'
})

st.header("Q21: Mediana Redação por raça")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=mediana_redacao_raca, x='Cor_Raca', y='Nota_Redacao', palette='Set3')
plt.title('Mediana de Redação por Cor/Raça')
plt.xticks(rotation=45)
st.pyplot(fig)

# Extrair valores para cada categoria
medianas = {
    'Amarela': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Amarela']['Nota_Redacao'].values[0],
    'Branca': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Branca']['Nota_Redacao'].values[0],
    'Indígena': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Indígena']['Nota_Redacao'].values[0],
    'Parda': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Parda']['Nota_Redacao'].values[0],
    'Preta': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Preta']['Nota_Redacao'].values[0],
    'Não declarado': mediana_redacao_raca[mediana_redacao_raca['Cor_Raca'] == 'Não declarado']['Nota_Redacao'].values[0]
}

st.markdown(f"""
**Resposta confirmada:** As medianas por raça são:
- Amarela: {medianas['Amarela']:.0f}
- Branca: {medianas['Branca']:.0f}
- Indígena: {medianas['Indígena']:.0f}
- Parda: {medianas['Parda']:.0f}
- Preta: {medianas['Preta']:.0f}
- Não declarado: {medianas['Não declarado']:.0f}
""")

# =============================================
# Q22: Maior desvio padrão em CH
# =============================================
desvio_ch_uf = df.groupby('UF_Escola')['Nota_Ciencias_Humanas'].std().sort_values(ascending=False).reset_index()
uf_maior_desvio_ch = desvio_ch_uf.iloc[0]['UF_Escola']
valor_desvio_ch = desvio_ch_uf.iloc[0]['Nota_Ciencias_Humanas']

st.header(f"Q22: Maior desvio padrão em CH: {uf_maior_desvio_ch}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=desvio_ch_uf, x='UF_Escola', y='Nota_Ciencias_Humanas', palette='viridis')
plt.title('Desvio Padrão de Ciências Humanas por Estado')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com maior desvio padrão em Ciências Humanas é '{uf_maior_desvio_ch}' com {valor_desvio_ch:.2f}.
""")

# =============================================
# Q23: Renda mais comum top 5% Redação
# =============================================
top_5_redacao = df.nlargest(int(len(df)*0.05), 'Nota_Redacao')
renda_top5_counts = top_5_redacao['Renda_Familiar'].value_counts().reset_index()
renda_top5_counts.columns = ['Renda_Familiar', 'Count']
renda_mais_comum_top5 = renda_top5_counts.iloc[0]['Renda_Familiar']
count_renda_top5 = renda_top5_counts.iloc[0]['Count']

st.header(f"Q23: Renda mais comum top 5% Redação: {renda_mais_comum_top5}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=renda_top5_counts, x='Renda_Familiar', y='Count', palette='viridis')
plt.title('Distribuição de Renda entre Top 5% em Redação')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A renda mais comum entre o top 5% em Redação é '{renda_mais_comum_top5}' com {count_renda_top5:,} participantes.
""")

# =============================================
# Q24: % notas 1000 Redação
# =============================================
total = len(df)
notas_1000 = len(df[df['Nota_Redacao'] == 1000])
percentual_1000 = (notas_1000 / total) * 100

st.header(f"Q24: % notas 1000 Redação: {percentual_1000:.4f}%")

fig, ax = plt.subplots(figsize=(8, 5))
plt.pie([percentual_1000, 100-percentual_1000], labels=['Nota 1000', 'Outras'], autopct='%1.4f%%', colors=['#ff9999','#66b3ff'])
plt.title('Proporção de Notas 1000 em Redação')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O percentual de notas 1000 em Redação é {percentual_1000:.4f}%.
""")

# =============================================
# Q25: Média MT por tipo de escola
# =============================================
media_mt_escola = df.groupby('TP_ESCOLA')['Nota_Matematica'].mean().reset_index()
media_mt_escola['TP_ESCOLA'] = media_mt_escola['TP_ESCOLA'].map({
    1: 'Não Respondeu', 2: 'Pública', 3: 'Exterior', 4: 'Privada'
})
media_publica_mt = media_mt_escola[media_mt_escola['TP_ESCOLA'] == 'Pública']['Nota_Matematica'].values[0]
media_privada_mt = media_mt_escola[media_mt_escola['TP_ESCOLA'] == 'Privada']['Nota_Matematica'].values[0]

st.header("Q25: Média MT por tipo de escola")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=media_mt_escola, x='TP_ESCOLA', y='Nota_Matematica', palette='Set2')
plt.title('Média de Matemática por Tipo de Escola')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** As médias por tipo de escola são:
- Pública: {media_publica_mt:.2f}
- Privada: {media_privada_mt:.2f}
""")

# =============================================
# Q26: Top 1% CN por sexo
# =============================================
top_1_cn = df.nlargest(int(len(df)*0.01), 'Nota_Ciencias_Natureza')
sexo_top1_counts = top_1_cn['Sexo'].value_counts(normalize=True).reset_index()
sexo_top1_counts.columns = ['Sexo', 'Percentual']
sexo_top1_counts['Percentual'] = sexo_top1_counts['Percentual'] * 100
percent_masc = sexo_top1_counts[sexo_top1_counts['Sexo'] == 'M']['Percentual'].values[0]
percent_fem = sexo_top1_counts[sexo_top1_counts['Sexo'] == 'F']['Percentual'].values[0]

st.header(f"Q26: Top 1% CN por sexo: Masc: {percent_masc:.1f}% - Fem: {percent_fem:.1f}%")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=sexo_top1_counts, x='Sexo', y='Percentual', palette='coolwarm')
plt.title('Distribuição por Sexo no Top 1% em Ciências da Natureza')
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A distribuição no top 1% em Ciências da Natureza é:
- Masculino: {percent_masc:.1f}%
- Feminino: {percent_fem:.1f}%
""")

# =============================================
# Q27: Faixa etária com maior média LC
# =============================================
media_lc_faixa = df.groupby('TP_FAIXA_ETARIA')['Nota_Linguagens'].mean().reset_index()
media_lc_faixa['Faixa_Etaria'] = media_lc_faixa['TP_FAIXA_ETARIA'].map(faixa_etaria_map)
media_lc_faixa = media_lc_faixa.sort_values('Nota_Linguagens', ascending=False)
faixa_maior_media_lc = media_lc_faixa.iloc[0]['Faixa_Etaria']
maior_media_lc_valor = media_lc_faixa.iloc[0]['Nota_Linguagens']

st.header(f"Q27: Faixa etária com maior média LC: {faixa_maior_media_lc}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_lc_faixa, x='Faixa_Etaria', y='Nota_Linguagens', palette='viridis')
plt.title('Média de Linguagens por Faixa Etária')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** A faixa etária com maior média em Linguagens é '{faixa_maior_media_lc}' com {maior_media_lc_valor:.2f} pontos.
""")

# =============================================
# Q28: Estado com maior média em CN
# =============================================
media_cn_uf = df.groupby('UF_Escola')['Nota_Ciencias_Natureza'].mean().sort_values(ascending=False).reset_index()
uf_maior_media_cn = media_cn_uf.iloc[0]['UF_Escola']
maior_media_cn_valor = media_cn_uf.iloc[0]['Nota_Ciencias_Natureza']

st.header(f"Q28: Estado com maior média em CN: {uf_maior_media_cn}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=media_cn_uf, x='UF_Escola', y='Nota_Ciencias_Natureza', palette='viridis')
plt.title('Média de Ciências da Natureza por Estado')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com maior média em Ciências da Natureza é '{uf_maior_media_cn}' com {maior_media_cn_valor:.2f} pontos.
""")

# =============================================
# Q29: Proporção de notas 1000 em Redação por tipo de escola
# =============================================
try:
    tipo_escola_map = {
        1: 'Não Respondeu',
        2: 'Pública',
        3: 'Exterior',
        4: 'Privada'
    }

    notas_1000 = df[df['Nota_Redacao'] == 1000]
    
    if len(notas_1000) == 0:
        st.warning("Nenhuma nota 1000 encontrada nos dados.")
    else:
        resultados = []
        for codigo, tipo in tipo_escola_map.items():
            total = len(df[df['TP_ESCOLA'] == codigo])
            total_1000 = len(notas_1000[notas_1000['TP_ESCOLA'] == codigo])
            percentual = (total_1000 / total) * 100 if total > 0 else 0
            resultados.append({
                'Tipo Escola': tipo,
                'Total Alunos': total,
                'Notas 1000': total_1000,
                'Percentual': percentual
            })

        df_resultados = pd.DataFrame(resultados)
        percent_publica = df_resultados[df_resultados['Tipo Escola'] == 'Pública']['Percentual'].values[0]
        percent_privada = df_resultados[df_resultados['Tipo Escola'] == 'Privada']['Percentual'].values[0]

        st.header(f"Q29: Proporção nota 1000 Redação: Pública: {percent_publica:.4f}% | Privada: {percent_privada:.4f}%")

        plt.figure(figsize=(10, 6))
        ax = sns.barplot(data=df_resultados, x='Tipo Escola', y='Percentual', 
                        palette='Set2', order=tipo_escola_map.values())
        plt.title('Percentual de Notas 1000 em Redação por Tipo de Escola', pad=15)
        plt.ylabel('Percentual (%)')
        plt.xlabel('')
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())
        plt.close()

        st.markdown(f"""
        **Resposta confirmada:** 
        - Pública: {percent_publica:.4f}%
        - Privada: {percent_privada:.4f}%
        """)

except Exception as e:
    st.error(f"Erro ao processar Q29: {str(e)}")

# =============================================
# Q30: Estado com maior diferença pública x privada (MT)
# =============================================
publicas = df[df['TP_ESCOLA'] == 2]
privadas = df[df['TP_ESCOLA'] == 4]

media_publica_uf = publicas.groupby('UF_Escola')['Nota_Matematica'].mean().reset_index()
media_privada_uf = privadas.groupby('UF_Escola')['Nota_Matematica'].mean().reset_index()

diferencas = pd.merge(media_privada_uf, media_publica_uf, on='UF_Escola', suffixes=('_privada', '_publica'))
diferencas['Diferenca'] = diferencas['Nota_Matematica_privada'] - diferencas['Nota_Matematica_publica']
diferencas = diferencas.sort_values('Diferenca', ascending=False)
uf_maior_diferenca = diferencas.iloc[0]['UF_Escola']
maior_diferenca_valor = diferencas.iloc[0]['Diferenca']

st.header(f"Q30: Estado com maior diferença pública x privada (MT): {uf_maior_diferenca}")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=diferencas, x='UF_Escola', y='Diferenca', palette='viridis')
plt.title('Diferença entre Médias de Matemática (Privada - Pública) por Estado')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown(f"""
**Resposta confirmada:** O estado com maior diferença entre escolas públicas e privadas em Matemática é '{uf_maior_diferenca}' com diferença de {maior_diferenca_valor:.2f} pontos.
""")

# =============================================
# Finalização
# =============================================
st.markdown("""
## Conclusão

Este painel apresenta visualizações que confirmam as respostas para as 30 questões analíticas sobre os microdados do ENEM 2018. 
Cada gráfico foi cuidadosamente construído para validar estatisticamente as respostas fornecidas.

**Observações:**
1. Todas as respostas foram calculadas dinamicamente a partir dos dados exibidos nos gráficos
2. Os resultados refletem a amostra específica de 660 mil participantes
3. Os dados consideram apenas participantes presentes em todas as provas
""")
