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

-- 데일리과제 1-4
CREATE TABLE users (
    name TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    balance TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
);

-- sqlite3 mydb.sqlite3
-- .mode csv
-- .import users.csv users

SELECT name, age, balance FROM users
ORDER BY age, balance DESC;


SELECT avg(balance) FROM users;