import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------- App Title --------
st.title(" Product Price Comparison App")

# -------- Input Section --------
product = st.text_input("Enter product name")

n = st.number_input("Enter number of shops", min_value=1, step=1)

shops = []
prices = []

st.subheader("Enter Shop Details")

for i in range(int(n)):
    shop = st.text_input(f"Shop {i+1} Name", key=f"shop_{i}")
    price = st.number_input(
        f"Price of {product} in Shop {i+1}",
        min_value=0.0,
        step=0.1,
        key=f"price_{i}"
    )
    
    if shop:
        shops.append(shop)
        prices.append(price)

# -------- Process Data --------
if st.button("Compare Prices"):
    if product and shops and prices:
        data = {
            "Shop": shops,
            "Price": prices
        }

        df = pd.DataFrame(data)

        # -------- Basic Statistics --------
        min_price = df["Price"].min()
        max_price = df["Price"].max()

        cheapest_shop = df[df["Price"] == min_price]
        expensive_shop = df[df["Price"] == max_price]

        # -------- Output --------
        st.subheader(f" Product: {product}")
        st.subheader(" Price Table")
        st.dataframe(df)

        st.subheader(" Cheapest Seller")
        st.dataframe(cheapest_shop)

        st.subheader(" Most Expensive Seller")
        st.dataframe(expensive_shop)

        # -------- Visualization --------
        st.subheader(" Price Comparison Chart")
        fig, ax = plt.subplots()
        ax.bar(df["Shop"], df["Price"])
        ax.set_xlabel("Shops")
        ax.set_ylabel("Price")
        ax.set_title(f"Price Comparison of {product}")
        st.pyplot(fig)
    else:
        st.warning("Please enter all details before comparing.")
