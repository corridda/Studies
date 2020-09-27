/*
Практика
1. Создайте базу данных bookstore.
2. Создайте схему bookstore и настройте путь поиска к ней
на уровне подключения к базе данных.
3. В схеме bookstore создайте таблицы для приложения
с необходимыми ограничениями целостности.
Точный список приведен в комментариях к слайду.
4. Вставьте в таблицы данные о нескольких книгах.
Проверьте себя с помощью запросов.
5. Зайдите в приложение. Видны ли в нем введенные данные?

books
	book_id	serial,	первичный ключ
	title	text

authors
	author_id	serial,	первичный ключ
	last_name	text
	first_name	text
	middle_name	text
	
authorship
	book_id		integer,	первичный ключ, внешний ключ для books
	author_id	integer,	первичный ключ, внешний ключ для authors
	seq_num		integer

operations
	operation_id	serial,		первичный ключ
	book_id		integer,	не NULL, внешний ключ для books
	qty_change	integer
	date_created	date,		текущая дата по умолчанию	
*/


-- Переключиться под суперпользователя
-- sudo su - postgres


-- Создайте базу данных bookstore.
CREATE DATABASE bookstore;
\c bookstore


-- Создайте схему bookstore и настройте путь поиска к ней
-- на уровне подключения к базе данных.
CREATE SCHEMA IF NOT EXISTS bookstore;
ALTER DATABASE bookstore SET search_path = bookstore, public;
\q
sudo pg_ctlcluster 9.6 main restart
psql
\c bookstore
show search_path;


-- В схеме bookstore создайте таблицы для приложения
-- с необходимыми ограничениями целостности.
-- books
CREATE TABLE IF NOT EXISTS books (
book_id serial PRIMARY KEY,
title text
);

-- authors
CREATE TABLE IF NOT EXISTS authors (
author_id serial PRIMARY KEY,
last_name text,
first_name text,
middle_name text
);

-- authorship
CREATE TABLE IF NOT EXISTS authorship (
book_id integer REFERENCES books (book_id),
author_id integer REFERENCES authors (author_id),
seq_num integer,
PRIMARY KEY (book_id, author_id)
);

-- operations
CREATE TABLE IF NOT EXISTS operations (
operation_id serial PRIMARY KEY,
book_id integer NOT NULL REFERENCES books (book_id),
qty_change integer,
date_created date DEFAULT CURRENT_DATE
);


-- Вставьте в таблицы данные о нескольких книгах.
-- Проверьте себя с помощью запросов.

-- books
INSERT INTO books(title) VALUES ('Сказка о царе Салтане');
INSERT INTO books(title) VALUES ('Муму');
INSERT INTO books(title) VALUES ('Трудно быть богом');
INSERT INTO books(title) VALUES ('Война и мир');
INSERT INTO books(title) VALUES ('Путешествия в некоторые удаленные страны мира в четырех частях: сочинение Лемюэля Гулливера, сначала хирурга, а затем капитана нескольких кораблей');
INSERT INTO books(title) VALUES ('Хрестоматия');

-- authors
INSERT INTO authors(last_name, first_name, middle_name) VALUES ('Пушкин', 'Александр', 'Сергеевич');
INSERT INTO authors(last_name, first_name, middle_name) VALUES ('Тургенев', 'Иван', 'Сергеевич');
INSERT INTO authors(last_name, first_name, middle_name) VALUES ('Стругацкий', 'Борис', 'Натанович');
INSERT INTO authors(last_name, first_name, middle_name) VALUES ('Стругацкий', 'Аркадий', 'Натанович');
INSERT INTO authors(last_name, first_name, middle_name) VALUES ('Толстой', 'Лев', 'Николаевич');
INSERT INTO authors(last_name, first_name) VALUES ('Свифт', 'Джонатан');

-- authorship
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(1, 1, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(2, 2, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(3, 3, 2);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(3, 4, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(4, 5, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(5, 6, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(6, 1, 1);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(6, 5, 2);
INSERT INTO authorship(book_id, author_id, seq_num) VALUES(6, 2, 3);
ANALYZE;

\x
SELECT * FROM books;
\x
SELECT * FROM authors;
SELECT * FROM authorship;

