SELECT query_name, ROUND(AVG(rating/position),2) as quality, ROUND(((SUM(rating < 3)/COUNT(query_name)) * 100),2) as poor_query_percentage
From Queries
Group BY query_name