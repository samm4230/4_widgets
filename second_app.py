import streamlit as st

st.title("Hello there")
st.header("A surprise to be sure, but a welcome one.")

slider = st.slider("This slides", 0, 500)

cities = ['Manchester', 'Tokyo', 'Brasilia', 'Ottawa', 'Wellington', 'Nairobi', 'Berlin']
st.selectbox('Choose a city', cities)
