import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

north = np.array([100,200,215,100,300,120,100,200,140,140,170,190])
south = np.array([150,100,115,200,250,150,210,150,160,150,180,200])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

total = north + south
total_with_months = list(zip(months, total)) # Combine months and total sales into a list of tuples/ It combines two lists position by position
average = np.mean(total)

growth = np.diff(total)
growth_months = months[1:]

st.write("Total Monthly Sales:")
for m, t in total_with_months:
    st.write(f"{m}: {t}")

st.write("Average Monthly Sales:", average)

st.write("Monthly Growth:")
for m, g in zip(growth_months, growth):
    st.write(f" {m}: {g}")

plt.plot(total)
st.pyplot(plt)