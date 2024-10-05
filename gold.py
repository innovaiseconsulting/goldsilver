import streamlit as st

# Constants for gold and silver prices
GOLD_PRICE = 7800
SILVER_PRICE = 1500

def calculate_price(metal_type, weight):
    if metal_type == "Gold":
        return weight * GOLD_PRICE
    elif metal_type == "Silver":
        return weight * SILVER_PRICE
    else:
        return 0

st.title("Gold and Silver Price Calculator")

st.write(f"Current Gold Price: ₹{GOLD_PRICE} per gram")
st.write(f"Current Silver Price: ₹{SILVER_PRICE} per gram")

metal_type = st.selectbox("Select Metal", ["Gold", "Silver"])

weight = st.number_input("Enter weight in grams", min_value=0.0, value=1.0, step=0.1)

if st.button("Calculate Price"):
    price = calculate_price(metal_type, weight)
    st.success(f"The price of {weight}g of {metal_type} is ₹{price:.2f}")

st.sidebar.header("About")
st.sidebar.info("This is a simple web application to calculate the price of gold and silver based on weight.")
st.sidebar.info("Prices used: Gold - ₹7800/g, Silver - ₹1500/g")
