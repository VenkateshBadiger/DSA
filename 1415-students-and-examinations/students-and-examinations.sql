SELECT s.student_id, s.student_name, sub.subject_name, count(ex.student_id) as attended_exams
FROM Students as s
CROSS JOIN Subjects as sub  
left JOIN Examinations as ex
on s.student_id = ex.student_id AND sub.subject_name = ex.subject_name
GROUP BY 
s.student_name, sub.subject_name, s.student_id
ORDER by s.student_id, sub.subject_name