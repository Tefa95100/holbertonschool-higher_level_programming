-- Lists all records of the table
-- when name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
