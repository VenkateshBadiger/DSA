SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) as average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND purchase_date between start_date AND end_date
GROUP BY p.product_id