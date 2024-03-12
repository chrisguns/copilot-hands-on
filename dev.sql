

-- define a select statement to get all students enrolled in a course
select s.first_name, s.last_name, s.email, r.registration_date, r.registration_status
from courses.students s
join courses.registrations r on s.student_id = r.student_id
where r.registration_status = 2 and r.course_id = 1;


-- write an index to improve the performance of the query
create index idx_registrations_course_id on courses.registrations (course_id, registration_status, registration_date);
```


