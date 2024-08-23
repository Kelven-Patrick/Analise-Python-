# Script de automação em Python
# Autor: Kelven Patrick Novaes Barbosa
# Data: 14-08-2024
# Descrição: Esse script feito em Python faz analise de dados e graficos interativo.

# Bibliotecas

# - `pip install pandas`
# - `pip install openpyxl`
# - `pip install plotly`
# - `pip install nbformat`

# importando bibliotecas
import pandas as pd

# Carregando os dados do Exel
dados = pd.read_excel("vendas.xlsx")

# Análises exploratórias

# visualizando as primeiras linhas
dados.head()

# visualizando as últimas linhas
dados.tail()

# formato da tabela de dados (linhas, colunas)
dados.shape

# visualizando informações das colunas
dados.info()

# Estatisticas

# selecionando e filtrando por colunas
dados[["cidade", "estado"]]

# informação do tipo de dados.
dados.describe()

# Análises

# contagem de vendas por loja
dados["loja"].value_counts()

# contagem de vendas por cidade
dados["cidade"].value_counts()

# contagem de vendas por formas de pagamento
dados["forma_pagamento"].value_counts()

# Agrupando Dados

# contagem de faturamento total por loja.
dados.groupby("loja")["preco"].sum().to_frame()

# contagem de faturamento agrupamento multiplo.
dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum().to_frame()

# Visualização de dados

# importa a biblioteca e atribui um alias
import plotly.express as px

# atribui a vareavel "grafico" com suas composições
grafico = px.histogram(
    dados,
    x="loja",
    y="preco",
    text_auto=True,
    title="Faturamento",
    color="forma_pagamento",
)

# mostra o grafico interativo quando chamar a variavel e o parametro "show"
grafico.show()

# exibe os dados em um grafico no formato "HTML" em seu browser.
grafico.write_html("Faturamento.html")

# Listas e o comando `for`

# variavel com lista de colunas
lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

# atribui cada nome da coluna a variavel "coluna" e printa em formato de grafico.
for coluna in lista_colunas:
    grafico = px.histogram(
        dados,
        x=coluna,
        y="preco",
        text_auto=True,
        title="Faturamento",
        color="forma_pagamento",
    )
    grafico.show()
    grafico.write_html(f"Faturamento{coluna}.html")

# variavel com lista de nomes
lista_nomes = ["Kelven", "Vinicios", "Pietro", "Cesar"]

# atribui cada nome da lista a variavel "nome" e printa em formato de lista
for nome in lista_nomes:
    print(nome)

print("Fim do Codigo!")
