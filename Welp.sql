/*
Welp
To practice what you’ve learned about joining multiple tables, you are going to use data from an exciting app called Welp. Users love Welp because it allows them to leave reviews of businesses in their city and see how other people reviewed the businesses.

For this project, you will be working with two tables:

places
reviews
Let’s get started!
*/



/* 
1. Let’s see what these tables contain by running the following commands: 
*/
SELECT * 
FROM places
;
SELECT * 
FROM reviews
;

/* 
2. If each dollar sign ($) represents $10, how could you find all places that cost $20 or less?

En la columna price_point
*/
SELECT address FROM places
WHERE price_point = '$' 
   OR price_point = '$$'
   ;

/*
3. What columns can be used to JOIN these two tables?
Write a query to do an INNER JOIN on the two tables to show all reviews for restaurants that have at least one review.
*/
SELECT * 
FROM places 
INNER JOIN reviews 
   ON places.id = reviews.place_id
   ;

/*
4. 
You probably noticed all the extra information in your results.

Modify your previous query to select only the most important columns in order to display a log of reviews
*/
SELECT places.name, places.average_rating, reviews.username, reviews.rating, reviews.review_date, reviews.note 
FROM places 
INNER JOIN reviews 
   ON places.id = reviews.place_id
LIMIT 20
;
-- UTILICE UN LIMIT PARA NO TENER UN RESULTADO TAN GRANDE

/*
5. Now write a query to do a LEFT JOIN on the tables, selecting the same columns as the previous question.

How are the results of this query different? Would this or the INNER JOIN be more useful for a log of reviews?
Encontramos algunos nulos, es mejor utilizar el INNER JOIN
*/
SELECT places.name, places.average_rating, reviews.username, reviews.rating, reviews.review_date, reviews.note 
FROM places 
LEFT JOIN reviews 
   ON places.id = reviews.place_id
LIMIT 20
;

/*
6. What about the places without reviews in our dataset?
*/
SELECT places.id, places.name 
FROM places 
LEFT JOIN reviews 
-- Utilizamos LEFT JOIN para encontrar los PLACES, de la tabla de PLACES, que no tengan coincidencia en la tabla REVIEWS
   ON places.id = reviews.place_id
WHERE reviews.note IS NULL
;

/*
7. Sometimes on Welp, there are some old reviews that aren’t useful anymore.

Write a query using the WITH clause to select all the reviews that happened in 2020. JOIN the places to your WITH query to see a log of all reviews from 2020.
*/
WITH reviews_2020 AS (
  SELECT * 
  FROM reviews
WHERE strftime ("%Y", review_date) = '2020'
)
SELECT * FROM places
INNER JOIN reviews_2020
ON places.id = reviews_2020.place_id
;

/*
8. Businesses want to be on the lookout for …ahem… difficult reviewers. Write a query that finds the reviewer with the most reviews that are BELOW the average rating for places.
*/
WITH average_rating AS (
  SELECT AVG(average_rating) as avg_rating
  FROM places
), bad_ratings AS(
  SELECT *, average_rating.avg_rating
  FROM reviews
  JOIN average_rating
  WHERE rating < avg_rating
), bad_ratings_per_user AS (
  SELECT username, COUNT(id) as "num_of_bad_ratings"
  FROM bad_ratings
  GROUP BY username
)
SELECT username, MAX(num_of_bad_ratings) as "bad_ratings"
FROM bad_ratings_per_user
;
