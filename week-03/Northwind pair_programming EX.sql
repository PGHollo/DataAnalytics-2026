USE northwind;

  SELECT categoryid, categoryname, description
  FROM categories;

SELECT productid, productname, quantityperunit
FROM products
WHERE quantityperunit LIKE '%box%';

SELECT productid, productname, discontinued
FROM products
WHERE discontinued =1;

SELECT CONCAT(firstname, ' ', lastname) AS 'FullName' , Title
FROM employees;

SELECT CustomerID, CompanyName, Country
FROM Customers
WHERE Country IN ('Germany', 'France');

SELECT COUNT(*) AS TotalOrders
FROM Orders;

SELECT SupplierID, CompanyName, ContactName, ContactTitle
FROM Suppliers
WHERE ContactTitle IN ('Sales Representative', 'Sales Manager');

SELECT OrderID, CustomerID, ShipCountry, ShippedDate
FROM Orders
WHERE ShipCountry = 'USA';

SELECT OrderID, CustomerID, RequiredDate, ShippedDate
FROM Orders
WHERE ShippedDate > RequiredDate;

SELECT ProductID, ProductName, UnitsInStock, ReorderLevel, Discontinued
FROM Products
WHERE UnitsInStock <= ReorderLevel
  AND Discontinued = 0;
  
  SELECT o.orderid,
  c.companyname as 'customer',
  o.Orderdate
  FROM Orders o
  JOIN Customers c ON o.customerid = c.Customerid
  ORDER BY o.orderdate DESC
  LIMIT 5;
  
  SELECT orderid, companyname, orderdate
  FROM orders
  Join Customers USING (Customerid)
  ORDER BY Orderdate
  Limit 5;
  
  SELECT p.productname,
  c.categoryname,
  p.unitprice
  FROM products p
  INNER JOIN categories c USING (categoryid)
  ORDER BY c.categoryname, p.productname
  LIMIT 6;
  
  SELECT c.companyname, 
		COUNT(o.Orderid) AS 'Order count'
  FROM customers c
  LEFT JOIN orders o ON c.customerid - o.customerid
  GROUP BY c.companyname
  ORDER BY `order count` ASC
  LIMIT 5;
  
  SELECT o.orderid,
  c.companyname as 'customer',
  o.Orderdate
  FROM Orders o
  JOIN Customers c ON o.customerid = c.Customerid
  ORDER BY o.orderdate DESC
  LIMIT 5;
  
  SELECT orderid, companyname, orderdate
  FROM orders
  Join Customers USING (Customerid)
  ORDER BY Orderdate
  Limit 5;