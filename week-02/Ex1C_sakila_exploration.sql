/*
a) Actor_ID, First_Name, Last_Name, Last_Update
b) Film_ID, Title, Description, Release_Year, LanguageID, OriginalLanguage, RentalDuration, RentalRate, Length, ReplacementCost, Rating, SpecialFeatures, Lastupdate
c) Film_Actor
d) RentalID, RentalDate, InventoryID, CustomerID, ReturnDate, StaffID, LastUpdate - Kind of hard to read beacuase it s all numerical data
e) InventoryID, FilmID, StoreID, LastUpdate - All numerical Data
f) We would need the film and rental tables. Film has the information containing the names and rental has the dates rented as well as the returned dates. They relate because they are joint tables!
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;

