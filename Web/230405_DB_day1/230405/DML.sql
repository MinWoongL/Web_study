CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTERGER NOT NULL
);



SELECT first_name, age FROM users;
SELECT rowid, first_name FROM users;
SELECT * FROM users;
