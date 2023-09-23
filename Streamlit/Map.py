import streamlit as st
import pandas as pd
import folium
import folium.plugins as plugins
import plotly.express as px

file_path = r"C:\Users\hp\Desktop\AUB\Courses\MSBA325 - Visualtion\Project 1\Project Plotly Rawad Salem\Data Sets\MAP.xlsx"
df = pd.read_excel(file_path)

st.sidebar.header("Custom Map Styling")
map_style = st.sidebar.selectbox("Select Map Style", ["Stamen Terrain", "OpenStreetMap", "CartoDB Positron"])

center_latitude = df['Latitude'].mean()
center_longitude = df['Longitude'].mean()
m = folium.Map(location=[center_latitude, center_longitude], zoom_start=6, tiles=map_style)

clustered = st.sidebar.checkbox("Enable Marker Clustering")
if clustered:
    plugins.MarkerCluster(locations=df[['Latitude', 'Longitude']]).add_to(m)

st.title('Earthquake Map')
st.write('Displaying earthquake data on a map')
st.write(m)

st.sidebar.header("Magnitude Histogram")
fig = px.histogram(df, x="Magnitude", nbins=20)
st.plotly_chart(fig)
