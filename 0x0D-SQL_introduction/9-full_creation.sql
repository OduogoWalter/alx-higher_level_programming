-- Script to create a table second_table and add multiple rows

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows
INSERT INTO hbtn_0c_0.second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);