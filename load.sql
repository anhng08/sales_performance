CREATE TABLE dim_customer AS
SELECT
    "Customer Index" AS customer_id,
    "Customer Names" AS customer_name
FROM customers;

CREATE TABLE dim_product AS
SELECT
    "Index" AS product_id,
    "Product Name" AS product_name
FROM products;

CREATE TABLE dim_region AS
SELECT
    id AS region_id,
    state,
    county,
    median_income,
    population
FROM regions;

CREATE TABLE dim_campaign AS
SELECT
    ROW_NUMBER() OVER () AS campaign_id,
    "Campaign Name",
    "Campaign Start",
    "Campaign End",
    "Region",
    "Strategy",
    "Cost"
FROM campaigns;

CREATE TABLE dim_channel AS
SELECT DISTINCT
    ROW_NUMBER() OVER () AS channel_id,
    "Channel"
FROM sales;

CREATE TABLE dim_date AS
SELECT DISTINCT
    DATE("OrderDate") AS date,
    EXTRACT(YEAR FROM "OrderDate") AS year,
    EXTRACT(MONTH FROM "OrderDate") AS month,
    EXTRACT(QUARTER FROM "OrderDate") AS quarter
FROM sales;

CREATE TABLE fact_sales AS
SELECT
    s."OrderNumber" AS order_id,
    d.date,
    c.customer_id,
    p.product_id,
    r.region_id,
    ch.channel_id,
    s."Order Quantity" AS quantity,
    s."Line Total" AS revenue,
    s."Total Unit Cost" AS cost,
    (s."Line Total" - s."Total Unit Cost") AS profit,
    (s."Line Total" - s."Total Unit Cost") / s."Line Total" AS margin
FROM sales s
LEFT JOIN dim_customer c
    ON s."Customer Name Index" = c.customer_id
LEFT JOIN dim_product p
    ON s."Product Description Index" = p.product_id
LEFT JOIN dim_region r
    ON s."Delivery Region Index" = r.region_id
LEFT JOIN dim_channel ch
    ON s."Channel" = ch.channel_name
LEFT JOIN dim_date d
    ON DATE(s."OrderDate") = d.date;