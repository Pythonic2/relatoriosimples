import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('pagamentos.csv')

st.header("Relatório SF Coffee")
st.sidebar.header("Escolha o relatório")
if st.sidebar.button("Relatório de vendas"):
    produtos_counts = df['Produtos'].explode().value_counts()

# # Visualizando os dados
    st.title("Relatório vendas")
    st.write(df)

    # Gráfico de formas de pagamento
    st.write("Gráfico de Formas de Pagamento:")
    forma_pagamento_counts = df['Forma pagamento '].value_counts()
    st.bar_chart(forma_pagamento_counts)

    # Gráfico de produtos
    st.write("Gráfico de Produtos:")
    st.bar_chart(produtos_counts)
    
if st.sidebar.button("Relatório de Ingredientes"):
    df_in = pd.read_csv('ingredientes.csv')
    st.write(df_in)
    st.bar_chart(df_in.set_index('ID')['Quantidade em estoque'])


# Processando os dados de produtos para contar o número de ocorrências de cada produto
