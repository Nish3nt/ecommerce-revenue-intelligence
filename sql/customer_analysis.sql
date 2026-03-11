-- Customer Lifetime Value

SELECT 
    c.customer_id,
    c.name,
    SUM(oi.quantity * p.price * (1 - oi.discount)) AS lifetime_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id
ORDER BY lifetime_value DESC
LIMIT 10 ;

-- Revenue Contribution by Category

SELECT 
    category,
    SUM(oi.quantity * p.price * (1 - oi.discount)) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY category
ORDER BY total_revenue DESC;

-- Discount Impact

SELECT 
    discount,
    SUM(quantity * price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY discount
ORDER BY discount;