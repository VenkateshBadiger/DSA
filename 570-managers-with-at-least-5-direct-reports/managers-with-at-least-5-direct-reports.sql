WITH manager AS(
    SELECT managerId, COUNT(*) as count
fROM Employee
Group by managerId
HAVING count >= 5)
SELECT e.name 
from Employee e
Join manager m ON e.id = m.managerId 

