SELECT 
  ROUND(SUM(
    CASE WHEN order_date = customer_pref_delivery_date then 1 
    ELSE 0 END
    )/COUNT(*),4) * 100 as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) in (SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY customer_id)


