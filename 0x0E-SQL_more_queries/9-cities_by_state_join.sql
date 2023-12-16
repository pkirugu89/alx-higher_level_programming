-- list all cities according to states
SELECT cities.id, cities.name, states.name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

