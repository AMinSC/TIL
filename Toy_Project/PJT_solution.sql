USE test1;
# a.
SELECT distinct S.ID, S.name as a
FROM takes as T
LEFT JOIN student as S
ON S.ID - T.ID
LEFT JOIN course as C
ON C.course_id = T.course_id
WHERE C.dept_name = 'Comp. Sci.' AND T.semester = 'Fall' AND T.year = 2010;

# b.
INSERT INTO course values ('CS-001', 'Weekly Seminar', 'Comp. Sci.', 1);
SELECT * FROM course;

# c.
INSERT INTO section values ('CS-001', 1, 'Fall', 2007, null, null, null);
SELECT * FROM section;
INSERT INTO takes
	SELECT ID, 'CS-001', 1, 'Fall', 2007, null
    FROM student
    WHERE dept_name = 'Comp. Sci.';
    
SELECT * FROM takes WHERE semester = 'Fall' AND year = 2007;

# d
SELECT name, dept_name, min(max_salary) as b
FROM(
	SELECT name, dept_name, max(salary) as max_salary
	FROM instructor
	GROUP BY dept_name, test1.instructor.name) as result
GROUP BY dept_name, result.name;
    
SELECT name, dept_name, max(salary) as max_salary
FROM instructor
GROUP BY dept_name, test1.instructor.name;

# e
SELECT distinct name as e
FROM instructor INNER JOIN teaches using (ID)
WHERE year = 2008 AND semester = 'Fall';

# f
SELECT distinct count(name) as f
FROM student INNER JOIN takes using (ID)
WHERE year = 2007 AND dept_name = 'Physics';
SELECT * FROM student;

# g
SELECT distinct S.name as student_name
FROM advisor AS A
INNER JOIN student AS S
  ON S.ID = s_ID
INNER JOIN instructor AS I
  ON I.ID = i_id
WHERE I.name = 'Lee' AND I.dept_name = 'Comp. Sci.' AND S.dept_name != 'Comp. Sci.';

# handler
SELECT distinct ID, name as h
FROM student
WHERE ID not in(
SELECT ID
FROM takes
WHERE year < 2010);
