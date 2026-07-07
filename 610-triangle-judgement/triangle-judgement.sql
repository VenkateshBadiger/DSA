SELECT x, y, z, 
(CASE WHEN x+y > z and z+y >x and z+x > y THEN 'Yes' ELSE 'No' END) AS triangle 
FROM Triangle 