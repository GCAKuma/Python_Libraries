import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Page setup ----------
st.set_page_config(page_title="Monthly Sales Dashboard", layout="wide")

# ---------- Data ----------
north = np.array([100, 200, 215, 100, 300, 120, 100, 200, 140, 140, 170, 190])
south = np.array([150, 100, 115, 200, 250, 150, 210, 150, 160, 150, 180, 200])

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# ---------- Calculations ----------
total = north + south
average = float(np.mean(total))
growth = np.diff(total)  # Feb..Dec (11 values)

# ---------- Create a DataFrame ----------
df = pd.DataFrame({
    "Month": months,
    "North": north,
    "South": south,
    "Total": total
})

# Add Growth column: Jan has no growth (NaN), Feb..Dec have values
df["Growth"] = np.nan
df.loc[1:, "Growth"] = growth

# ---------- UI ----------
st.title("📊 Monthly Sales Dashboard")

# KPI cards
c1, c2, c3 = st.columns(3)
c1.metric("Average Monthly Sales", f"{average:.2f}")
c2.metric("Highest Total Month", f"{df.loc[df['Total'].idxmax(), 'Month']}", f"{df['Total'].max()}")
c3.metric("Lowest Total Month", f"{df.loc[df['Total'].idxmin(), 'Month']}", f"{df['Total'].min()}")

st.divider()

# Filter slider
threshold = st.slider(
    "Show months where Total sales are above:",
    min_value=0,
    max_value=int(df["Total"].max()),
    value=100,
    step=10
)

filtered = df[df["Total"] > threshold]

# Tables
left, right = st.columns([1.1, 1])

with left:
    st.subheader("🧾 All Months (Table)")
    st.dataframe(df, use_container_width=True)

with right:
    st.subheader("🔎 Filtered Months (Table)")
    st.dataframe(filtered, use_container_width=True)

st.divider()

# ---------- Charts ----------
colA, colB = st.columns(2)

with colA:
    st.subheader("📈 Total Sales Trend")
    fig1, ax1 = plt.subplots()
    ax1.plot(df["Month"], df["Total"], marker="o")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Sales")
    ax1.set_title("Total Sales by Month")
    st.pyplot(fig1)

with colB:
    st.subheader("📊 Monthly Growth (Feb → Dec)")
    fig2, ax2 = plt.subplots()
    ax2.bar(df["Month"][1:], df["Growth"][1:])  # Growth starts from Feb
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Growth (This month - Previous month)")
    ax2.set_title("Month-to-Month Growth")
    st.pyplot(fig2)