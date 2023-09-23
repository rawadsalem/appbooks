import pandas as pd
import plotly.express as px
import streamlit as st

file_path = 'C:/Users/hp/Desktop/Data Sets/Consoles Data.csv'
df = pd.read_csv(file_path)

st.title('Consoles Sold Worldwide')

st.sidebar.header('Customize Visualization')
selected_column = st.sidebar.selectbox('Select Column:', df.columns)

fig = px.bar(
    df,
    x='Company',
    y='Units sold (million)',
    color='Console Name',
    title=f'Total Units Sold by Company for Different Consoles - {selected_column}',
    labels={'Company': 'Company', 'Units sold (million)': 'Units Sold (Million)'}
)

fig.update_xaxes(title='Company')
fig.update_yaxes(title='Units Sold (Million)')

st.plotly_chart(fig)


