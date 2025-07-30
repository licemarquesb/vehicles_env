import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles.csv')
st.title('Análise de Vendas de Veículos')
option = st.selectbox(
    'Selecione o tipo de gráfico que deseja visualizar:',
    ('Histograma', 'Dispersão') 
)

#gerando o gráfico com base na opção selecionada
if option == 'Histograma':
    st.write('Histograma da Quilometragem')
    fig = px.histogram(car_data, x='odometer', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Dispersão':
    st.write('Dispersão: Quilometragem X Preço')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

