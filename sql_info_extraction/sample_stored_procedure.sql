CREATE PROCEDURE GetEmployeeDetails
    @EmployeeId INT,
    @DepartmentId INT
AS
BEGIN

    SELECT EmployeeId, Name, Salary
    FROM Employees
    WHERE EmployeeId = @EmployeeId;

    UPDATE Employees
    SET Salary = Salary * 1.10
    WHERE EmployeeId = @EmployeeId;

END;