import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input Section 
n = int(input("Enter number of shops: "))

shops = []
prices = []

product = input("Enter product name: ")

for i in range(n):
    shop = input(f"Enter shop {i+1} name: ")
    price = float(input(f"Enter price of {product} in {shop}: "))
    
    shops.append(shop)
    prices.append(price)

# Data Creation 
data = {
    "Shop": shops,
    "Price": prices
}

df = pd.DataFrame(data)

#  Basic Statistics 
min_price = df["Price"].min()
max_price = df["Price"].max()

cheapest_shop = df[df["Price"] == min_price]
expensive_shop = df[df["Price"] == max_price]

# Output
print("\nProduct:", product)
print("\nPrice Table:")
print(df)

print("\nCheapest Seller:")
print(cheapest_shop)

print("\nMost Expensive Seller:")
print(expensive_shop)

# Visualization
plt.bar(df["Shop"], df["Price"])
plt.xlabel("Shops")
plt.ylabel("Price")
plt.title(f"Price Comparison of {product}")
plt.show()




