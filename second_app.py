import streamlit as st

st.title("Hello there")
st.header("A surprise to be sure, but a welcome one.")

first_name = st.text_input('What is your first name?')
print(f'Hi {first_name} :smile:')

slider = st.slider("This slides", 0, 500)

cities = ['Manchester', 'Tokyo', 'Brasilia', 'Ottawa', 'Wellington', 'Nairobi', 'Berlin']
st.selectbox('Choose a city', cities)

button1 = st.button('Press for cold')
if button1:
  st.snow()

button2 = st.button('Press for helium')
if button2:
  st.balloons()
