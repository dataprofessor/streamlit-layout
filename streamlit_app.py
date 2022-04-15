import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('How do you feel?', ['', 'happy', 'tired', 'excited'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'Hello {user_name}')
  else:
    st.write('👈  Please enter your **name** in the sidebar!')

with col2:
  if user_emoji != '':
    st.write(user_emoji)
  else:
    st.write('👈 Please choose an **emoji** in the sidebar')
