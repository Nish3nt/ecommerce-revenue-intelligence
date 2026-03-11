import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///database/ecommerce.db")

print("Connected to SQLite database")

# Load CSV files
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")
payments = pd.read_csv("data/raw/payments.csv")
reviews = pd.read_csv("data/raw/reviews.csv")

# Insert data into database
customers.to_sql("customers", engine, if_exists="replace", index=False)
print("Customers loaded")

products.to_sql("products", engine, if_exists="replace", index=False)
print("Products loaded")

orders.to_sql("orders", engine, if_exists="replace", index=False)
print("Orders loaded")

order_items.to_sql("order_items", engine, if_exists="replace", index=False)
print("Order items loaded")

payments.to_sql("payments", engine, if_exists="replace", index=False)
print("Payments loaded")

reviews.to_sql("reviews", engine, if_exists="replace", index=False)
print("Reviews loaded")

print("All data loaded successfully into SQLite database")