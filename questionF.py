import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
"Product":["Rice","Milk","Eggs","Bread"],
"Jan":[120,80,20,60],
"Feb":[150,50,30,70],
"Mar":[130,60,25,45]
}

df = pd.DataFrame(data)
df["Total"] = df["Jan"] + df["Feb"] + df["Mar"]

st.dataframe(df)

threshold = st.slider("Filter Sales Above", 0, 400, 100)
filtered = df[df["Total"] > threshold]

st.dataframe(filtered)

plt.bar(filtered["Product"], filtered["Total"])
st.pyplot(plt)