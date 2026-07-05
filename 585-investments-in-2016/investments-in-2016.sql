Select rounD(sum(tiv_2016),2) as tiv_2016 
From Insurance 
WHERE (lat, lon) IN (
    SELECT lat, lon
    from Insurance 
    GROUP BY lat, lon 
    Having count(*) = 1
)
AND tiv_2015 IN (
    SELECT tiv_2015
    FROM insurance 
    GROUP BY tiv_2015
    HAVING COUNT(*)>1
)