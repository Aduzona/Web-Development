CREATE TABLE `if NOT Exists Book (
    id serial PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price Float NOT NULL
  );