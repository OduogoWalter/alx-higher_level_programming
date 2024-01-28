-- Script to print the full description of the table first_table from the database hbtn_0c_0

SELECT CONCAT('Table   ', table_name, '\t', 'Create Table') AS Description
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
