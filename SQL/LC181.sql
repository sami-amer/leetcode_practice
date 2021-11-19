# Employees earning more than their manager (one table)
SELECT E1.Name AS Employee
FROM Employee AS E1,Employee AS E2
WHERE E1.ManagerId=E2.Id AND E1.Salary>E2.Salary;