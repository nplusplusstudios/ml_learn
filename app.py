#import streamlit as st
#import pandas as pd
#import numpy as np

#st.write("Hello **world!* :sunglasses:")
#x = st.text_input("Favorite Movie?")
#st.write(f"Your Favorite Movie is : {x}")

#data = pd.read_csv("imdb_top_1000.csv")
#st.write(data)

#st.write("# My Cool Chart")

#chart_data = pd.DataFrame(
#  np.random.randn(20,3),
#  columns=["a","b","c"]
#)

#st.bar_chart(chart_data)
#st.line_chart(chart_data)
#st.pie_chart(chart_data)
#st.write("practing again..")

#---------------- pasting code from chatGPT for testing perpose

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# Sample training data
data = {
    "soil_moisture": [20,30,40,70,80,90],
    "temperature": [35,32,30,25,24,22],
    "health": ["Dry","Dry","Healthy","Healthy","Overwatered","Overwatered"]
}

df = pd.DataFrame(data)


# ML model
X = df[["soil_moisture","temperature"]]
y = df["health"]

model = DecisionTreeClassifier()
model.fit(X,y)


# Streamlit UI
st.title("🌱 Smart Plant Health Predictor")

st.write("Enter plant conditions")

moisture = st.slider(
    "Soil Moisture",
    0,100,50
)

temp = st.slider(
    "Temperature",
    10,50,30
)


if st.button("Predict"):

    result = model.predict(
        [[moisture,temp]]
    )

    st.success(
        "Plant Status: " + result[0]
    )

