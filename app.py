import streamlit as st
import pandas as pd

st.write("Hello **world!* :sunglasses:")
x = st.text_input("Favorite Movie?")
st.write(f"Your Favorite Movie is : {x}")

data = pd.read_csv("imdb_top_1000.csv")
st.write(data)
