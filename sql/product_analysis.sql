-- Top Revenue Generating Products

SELECT 
    p.product_name,
    p.category,
    SUM(oi.quantity * p.price * (1 - oi.discount)) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY revenue DESC
LIMIT 10;