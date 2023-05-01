import pandas as pd
import plotly.express as px
import streamlit as st
# importando a bse
df = pd.read_csv('ocor_1746_31abril.csv', sep = ';')



bairros = list(df['nome'].unique())
bairro = st.sidebar.selectbox('Bairro', bairros) # Baixa  de seleção no menu lateral usando duas funções

colunas = 'id_chamado'
column = st.sidebar.selectbox('Chamados', colunas)

# Grafico
fig = px.line(df, x = 'data_inicio', y = 'id_chamado', title = column + ' - ' + bairro )
fig.update_layout( xaxis_title = 'Data', yaxis_title = column.upper(), title = {'x':0.5})


# Colocando um titulo
st.title('Ocorrências no 1746 por Bairros na Cidade do Rio de Janeiro')

# Texto menor e normal
st.write('O Grafico Abaixo fala sobre Ocorrências no 1746')

st.caption('Produzido por Christian Basilio')

st.plotly_chart(fig, use_contrainer_width = True)

fig.show()