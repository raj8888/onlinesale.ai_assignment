SELECT d.NAME AS DEPT_NAME, AVG(s.AMT) AS AVG_MONTHLY_SALARY
FROM departments d
JOIN employees e ON d.ID = e.DEPT_ID
JOIN salaries s ON e.ID = s.EMP_ID
GROUP BY d.ID, d.NAME
ORDER BY AVG_MONTHLY_SALARY DESC
LIMIT 3;

-- This query joins the Departments, Employees, and salaries tables using foreign key relationships.
-- It calculates the average salaries (AVG) for each department and retrieves the department name (d.NAME)
-- The result is sorted in descending order by the average monthly salary and limited to the top 3 rows using LIMIT.


