-- Script to list records of second_table with names, ordered by descending score

SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
