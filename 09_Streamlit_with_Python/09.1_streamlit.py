import streamlit as st
import pandas as pd
import numpy as np

# Title of the Application

st.title('Hamza Workstation')

# Display a simple text

st.write('This is a simple task')

# Create a simple Dataframe

df = pd.DataFrame({
    'first column' : [1 , 2 , 3 , 4],
    'second column' : [10 , 20 , 30 , 40]
})

# Display the dataframe

st.write('Here is the dataframe')
st.write(df)

# create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20 , 3) , columns = ['a' , 'b' , 'c']
)

st.line_chart(chart_data)

print(dir(st))
print('line_chart' in dir(st))