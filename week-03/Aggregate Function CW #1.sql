USE sakila;

-- Find the total number of payments made in the database.

SELECT COUNT(*) AS Totalpayments
FROM payment;

-- A query to calculate total sales from june 2005 to highlight higher or lesser grossing sales during that specific timeframe 

SELECT COUNT(*) AS TotalPaymentsInJune
FROM payment
WHERE payment_date BETWEEN '2005-06-01' AND '2005-06-30'