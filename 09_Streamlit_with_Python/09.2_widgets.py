import streamlit as st
import pandas as pd

st.title('Streamlit text Input')

name = st.text_input('Enter your name : ')

if name:
    
    st.write(f'Assalamo Alikum , {name}')

age = st.slider('Select your age : ' , 0 , 100 , 20)

st.write(f'Your age is {age}')

options = ["Python" , "Java" , "C++" , "JavaScript"]

choice = st.selectbox('Choose Your Favourite Language : ' , options)

st.write(f'You selected {choice}')

data = {
    
    "Name" : ["John" , "Jane" , "Jake" , "Jill"],
    "Age": [28 , 24 , 35 , 40],
    "City": ["New York" , "Los Angeles" , "Chicago" , "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

df.to_csv('sampledata.csv')

uploaded_file = st.file_uploader('Choose a CSV file' , type = 'CSV')

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.write(df) 