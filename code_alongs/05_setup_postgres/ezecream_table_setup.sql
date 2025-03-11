CREATE SCHEMA IF NOT EXISTS ezecream_05;

SET search_path TO ezecream_05;

CREATE TABLE IF NOT EXISTS Customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    personal_number CHAR(12),
    email VARCHAR(255) NOT NULL,
    address VARCHAR(100) NOT NULL
);