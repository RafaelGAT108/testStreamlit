import pandas as pd
import numpy as np
import streamlit as st

data = pd.read_csv("melb_data.csv")
data = data.drop(['Suburb', 'Address', 'SellerG', 'Date'], axis=1)
data = data.drop(['BuildingArea', 'YearBuilt'], axis=1)

st.write("Here's our first attempt at using data to create a table:")
st.write(data)

uploaded_file = st.file_uploader("Choose a file")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)