SELECT MONTH(OrderDate) AS Month, SUM(Revenue) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Month;

SELECT Product, SUM(Revenue) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 10;
