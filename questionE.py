import streamlit as st
import pandas as pd

st.title("Price Elasticity of Demand (PED) Calculator")

data = {
"Product":["Rice","Milk","Bread","Eggs"],
"Q1":[100,80,60,150],
"Q2":[120,70,65,180],
"P1":[50,40,20,30],
"P2":[55,45,25,35]
} # Create a dictionary to hold the data for products, quantities, and prices

df = pd.DataFrame(data) # Create a DataFrame from the data dictionary

df["%Change_Q"] = (df["Q2"] - df["Q1"]) / df["Q1"] # make a new column for % change in quantity
df["%Change_P"] = (df["P2"] - df["P1"]) / df["P1"] # make a new column for % change in price
df["PED"] = df["%Change_Q"] / df["%Change_P"] # make a new column for PED using the formula

st.dataframe(df) # Display the DataFrame with calculated new columns

slider = st.slider("Filter PED > ", 0.0, 2.0, 1.0) # Create a slider to select PED threshold

filtered = df[df["PED"] > slider]
# filtered = df[condition]
# condition = df["PED"] > slider
# Create a NEW DataFrame using rows where condition is True
          # OLD TABLE (df)
          #         ↓ (apply condition)
          # NEW TABLE (filtered)


st.write("Filtered Products")
st.dataframe(filtered) # Display the filtered DataFrame based on the slider value