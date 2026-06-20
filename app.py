import streamlit as st
import pandas as pd
import numpy as np

#st.write("Hello **world!* :sunglasses:")
#x = st.text_input("Favorite Movie?")
#st.write(f"Your Favorite Movie is : {x}")

#data = pd.read_csv("imdb_top_1000.csv")
#st.write(data)

st.write("# My Cool Chart")

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
st.pie_chart(chart_data)
st.write("practing again..")


