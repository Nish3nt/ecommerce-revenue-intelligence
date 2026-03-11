import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

# Create directories if not present
os.makedirs("data/raw", exist_ok=True)

NUM_CUSTOMERS = 50000
NUM_PRODUCTS = 2000
NUM_ORDERS = 300000

# -----------------------------
# CUSTOMERS DATA
# -----------------------------

customers = []

for i in range(NUM_CUSTOMERS):
    customers.append([
        f"CUST_{i}",
        fake.name(),
        random.choice(["Male","Female"]),
        fake.city(),
        fake.state(),
        fake.date_between(start_date="-3y", end_date="today")
    ])

customers_df = pd.DataFrame(customers, columns=[
    "customer_id",
    "name",
    "gender",
    "city",
    "state",
    "signup_date"
])

customers_df.to_csv("data/raw/customers.csv", index=False)


# -----------------------------
# PRODUCTS DATA
# -----------------------------

categories = ["Electronics","Fashion","Home","Sports","Beauty"]

products = []

for i in range(NUM_PRODUCTS):
    products.append([
        f"PROD_{i}",
        fake.word(),
        random.choice(categories),
        round(random.uniform(10,1000),2)
    ])

products_df = pd.DataFrame(products, columns=[
    "product_id",
    "product_name",
    "category",
    "price"
])

products_df.to_csv("data/raw/products.csv", index=False)


# -----------------------------
# ORDERS DATA
# -----------------------------

orders = []

for i in range(NUM_ORDERS):
    orders.append([
        f"ORD_{i}",
        f"CUST_{random.randint(0, NUM_CUSTOMERS-1)}",
        fake.date_between(start_date="-2y", end_date="today")
    ])

orders_df = pd.DataFrame(orders, columns=[
    "order_id",
    "customer_id",
    "order_date"
])

orders_df.to_csv("data/raw/orders.csv", index=False)

print("Dataset generation completed.")