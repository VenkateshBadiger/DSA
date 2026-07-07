WITH n as(
    SELECT employee_id, department_id 
FROM Employee 
GROUP BY employee_id
HAVING COUNT(employee_id) = 1
),
y as(
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'
)
SELECT * FROM n
UNION
SELECT * FROM y;