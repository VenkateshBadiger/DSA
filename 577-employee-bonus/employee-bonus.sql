SELECT e.name, b.bonus
FROM Employee AS e LEFT JOIN Bonus as b
on e.empId= b.empId
WHERE b.bonus < 1000 OR bonus is Null