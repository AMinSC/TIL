SELECT name, dept_name, MIN(MAX_salary)
FROM (SELECT name, dept_name, MAX(salary) as MAX_salary
	  FROM instructor
	  GROUP BY dept_name) as st;