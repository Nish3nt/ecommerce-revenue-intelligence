import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

# -----------------------------
# Create folders if not present
# -----------------------------

os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# Dataset Sizes
# -----------------------------

NUM_CUSTOMERS = 50000
NUM_PRODUCTS = 2000
NUM_ORDERS = 300000
NUM_ORDER_ITEMS = 700000
NUM_REVIEWS = 150000

# -----------------------------
# CUSTOMERS
# -----------------------------

customers = []

for i in range(NUM_CUSTOMERS):
    customers.append([
        f"CUST_{i}",
        fake.name(),
        random.choice(["Male", "Female"]),
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

print("Customers dataset generated")

# -----------------------------
# PRODUCTS
# -----------------------------

categories = ["Electronics", "Fashion", "Home", "Sports", "Beauty"]

products = []

for i in range(NUM_PRODUCTS):
    products.append([
        f"PROD_{i}",
        fake.word(),
        random.choice(categories),
        round(random.uniform(10, 1000), 2)
    ])

products_df = pd.DataFrame(products, columns=[
    "product_id",
    "product_name",
    "category",
    "price"
])

products_df.to_csv("data/raw/products.csv", index=False)

print("Products dataset generated")

# -----------------------------
# ORDERS
# -----------------------------

orders = []

for i in range(NUM_ORDERS):
    orders.append([
        f"ORD_{i}",
        f"CUST_{random.randint(0, NUM_CUSTOMERS - 1)}",
        fake.date_between(start_date="-2y", end_date="today")
    ])

orders_df = pd.DataFrame(orders, columns=[
    "order_id",
    "customer_id",
    "order_date"
])

orders_df.to_csv("data/raw/orders.csv", index=False)

print("Orders dataset generated")

# -----------------------------
# ORDER ITEMS
# -----------------------------

order_items = []

for i in range(NUM_ORDER_ITEMS):
    order_items.append([
        f"ITEM_{i}",
        f"ORD_{random.randint(0, NUM_ORDERS - 1)}",
        f"PROD_{random.randint(0, NUM_PRODUCTS - 1)}",
        random.randint(1, 5),
        round(random.uniform(0, 0.3), 2)
    ])

order_items_df = pd.DataFrame(order_items, columns=[
    "order_item_id",
    "order_id",
    "product_id",
    "quantity",
    "discount"
])

order_items_df.to_csv("data/raw/order_items.csv", index=False)

print("Order items dataset generated")

# -----------------------------
# PAYMENTS
# -----------------------------

payment_methods = ["Credit Card", "Debit Card", "UPI", "Wallet"]

payments = []

for i in range(NUM_ORDERS):
    payments.append([
        f"PAY_{i}",
        f"ORD_{i}",
        random.choice(payment_methods),
        round(random.uniform(20, 2000), 2)
    ])

payments_df = pd.DataFrame(payments, columns=[
    "payment_id",
    "order_id",
    "payment_method",
    "payment_value"
])

payments_df.to_csv("data/raw/payments.csv", index=False)

print("Payments dataset generated")

# -----------------------------
# REVIEWS
# -----------------------------

reviews = []

for i in range(NUM_REVIEWS):
    reviews.append([
        f"REV_{i}",
        f"PROD_{random.randint(0, NUM_PRODUCTS - 1)}",
        f"CUST_{random.randint(0, NUM_CUSTOMERS - 1)}",
        random.randint(1, 5),
        fake.date_between(start_date="-1y", end_date="today")
    ])

reviews_df = pd.DataFrame(reviews, columns=[
    "review_id",
    "product_id",
    "customer_id",
    "rating",
    "review_date"
])

reviews_df.to_csv("data/raw/reviews.csv", index=False)

print("Reviews dataset generated")

print("All datasets generated successfully!")