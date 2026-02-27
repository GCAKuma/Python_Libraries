import streamlit as st

st.title("Simple Interest Calculator")

P = st.number_input("Enter Principal Amount")
R = st.number_input("Enter Annual Interest Rate (%)")
T = st.number_input("Enter Time Period (Years)")

if st.button("Calculate", key="calc_1"):
    SI = (P * R * T) / 100
    st.write("Simple Interest LKR", SI)

st.title("Compound Amount Calculator")

P = st.number_input("Principal Amount")
R = st.number_input("Annual Interest Rate (%)")
T = st.number_input("Time Period (Years)")

if st.button("Calculate", key="calc_2"):
    A = P * (1 + R/100) ** T
    st.write("Compound Amount LKR", A)

st.title("Price Elasticity Calculator")

q1 = st.number_input("Q1")
q2 = st.number_input("Q2")
p1 = st.number_input("P1")
p2 = st.number_input("P2")

if st.button("Calculate", key="calc_3"):
    percent_q = (q2 - q1) / q1
    percent_p = (p2 - p1) / p1
    elasticity = percent_q / percent_p
    st.write("Elasticity:", round(elasticity,2))


st.title("Business Calculator")

option = st.selectbox("Select Method",
["Total Cost","Average Cost","Total Profit"])

if option == "Total Cost":
    fixed = st.number_input("Fixed Cost")
    variable = st.number_input("Variable Cost per Unit")
    units = st.number_input("Units Produced")
    if st.button("Calculate"):
        total = fixed + (variable * units)
        st.write("Total Cost LKR", total)

elif option == "Average Cost":
    total = st.number_input("Total Cost")
    units = st.number_input("Units")
    if st.button("Calculate"):
        avg = total / units
        st.write("Cost of Unit LKR", avg)

elif option == "Total Profit":
    sp = st.number_input("Selling Price")
    cp = st.number_input("Cost Price")
    units = st.number_input("Units Sold")
    if st.button("Calculate" ,key="calc_4"):
        profit = (sp - cp) * units
        st.write("Total Profit LKR", profit)