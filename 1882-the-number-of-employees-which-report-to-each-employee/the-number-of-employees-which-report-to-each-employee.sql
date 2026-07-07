SELECT e.employee_id, e.name, COUNT(e2.reports_to) as reports_count, ROUND(AVG(e2.age)) as average_age
FROM Employees e
LEFT JOIN Employees e2 ON e.employee_id = e2.reports_to
GROUP BY employee_id
HAVING reports_count > 0 
ORDER BY e.employee_id