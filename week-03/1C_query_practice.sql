USE northwind;

SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice ASC;

SELECT ProductID, ProductName, UnitsInStock, UnitPrice
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

SELECT ProductID, ProductName, UnitsInStock, UnitPrice
FROM Products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders;

SELECT ShipCountry,
       COUNT(DISTINCT CustomerID) AS CustomerCount
FROM Orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM Products
WHERE UnitsInStock < 25
  AND UnitsOnOrder > 0
ORDER BY UnitsOnOrder DESC, ProductName ASC;

SELECT Title, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Title;

SELECT EmployeeID, FirstName, LastName, Title, Salary
FROM Employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;