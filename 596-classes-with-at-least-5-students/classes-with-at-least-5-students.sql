SELECT class 
FROM Courses
GROUP by class
having count(distinct student)>=5