import streamlit as st
import pandas as pd

st.title("Price Elasticity of Demand (PED) Calculator")

data = {
"Product":["Rice","Milk","Bread","Eggs"],
"Q1":[100,80,60,150],
"Q2":[120,70,65,180],
"P1":[50,40,20,30],
"P2":[55,45,25,35]
}

df = pd.DataFrame(data)

df["%Change_Q"] = (df["Q2"] - df["Q1"]) / df["Q1"]
df["%Change_P"] = (df["P2"] - df["P1"]) / df["P1"]
df["PED"] = df["%Change_Q"] / df["%Change_P"]

st.dataframe(df)

slider = st.slider("Filter PED > ", 0.0, 2.0, 1.0)
filtered = df[df["PED"] > slider]

st.write("Filtered Products")
st.dataframe(filtered)