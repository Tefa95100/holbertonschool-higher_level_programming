-- Lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.states = states.id
ORDER BY cities.id ASC;
