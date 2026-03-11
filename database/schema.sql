CREATE TABLE customers (
    customer_id VARCHAR PRIMARY KEY,
    name TEXT,
    gender TEXT,
    city TEXT,
    state TEXT,
    signup_date DATE
);

CREATE TABLE products (
    product_id VARCHAR PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price FLOAT
);

CREATE TABLE orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id VARCHAR PRIMARY KEY,
    order_id VARCHAR,
    product_id VARCHAR,
    quantity INT,
    discount FLOAT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id VARCHAR PRIMARY KEY,
    order_id VARCHAR,
    payment_method TEXT,
    payment_value FLOAT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE reviews (
    review_id VARCHAR PRIMARY KEY,
    product_id VARCHAR,
    customer_id VARCHAR,
    rating INT,
    review_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);