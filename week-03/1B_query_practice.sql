
/* Write a query to list the product id, product name, and unit price of every product that
Northwind sells. (Hint: To help set up your query, look at the schema preview to see
what column names belong to each table. Or use SELECT * to query all columns
first, then refine your query to just the columns you want.)
*/

USE northwind;

SELECT productname, unitprice 
FROM products; 

SELECT productname, unitprice
FROM products
WHERE unitprice <= 7.50;

SELECT productid, productname, unitsinstock, unitsonorder
FROM products
WHERE unitsinstock = 0
  AND unitsonorder > 0;
  
  SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM Products p
JOIN Categories c
USING (CategoryID)
WHERE c.CategoryName = 'Seafood';

SELECT p.ProductID, p.ProductName, p.UnitPrice
FROM Products p
JOIN Suppliers s
USING (SupplierID)
WHERE s.CompanyName = 'Tokyo Traders';

SELECT EmployeeID, FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%manager%';


  
  
  
  
  
  


