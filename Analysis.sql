-- 1. Har order ka net revenue nikalna (discount ke baad)
SELECT
    order_id,
    order_date,
    region,
    category,
    product,
    quantity,
    unit_price,
    discount_pct,
    ROUND((quantity * unit_price) * (1 - discount_pct / 100.0), 2) AS net_revenue
FROM sales_data
ORDER BY order_date;

-- 2. Region-wise total revenue aur total orders
SELECT
    region,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM((quantity * unit_price) * (1 - discount_pct / 100.0)), 2) AS total_revenue
FROM sales_data
GROUP BY region
ORDER BY total_revenue DESC;

-- 3. Category-wise performance summary
SELECT
    category,
    SUM(quantity) AS units_sold,
    ROUND(AVG(unit_price), 2) AS avg_unit_price,
    ROUND(SUM((quantity * unit_price) * (1 - discount_pct / 100.0)), 2) AS category_revenue
FROM sales_data
GROUP BY category
ORDER BY category_revenue DESC;
