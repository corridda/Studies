/*
Практика
1.	Какие дополнительные атрибуты могут появиться
	у выделенных сущностей при развитии приложения?
2.	Допустим, требуется хранить информацию об издательстве.
	Дополните ER-диаграмму и отобразите ее в таблицы.
3.	Некоторые книги могут входить в серии (например,
	«Библиотека приключений»). Как изменится схема данных?
	Разные издательства вполне могут иметь серии, названные
	одинаково.

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


-- Подключиться к базе данных 'bookstore'.
\c bookstore


-- Допустим, требуется хранить информацию об издательстве.
-- Дополните ER-диаграмму и отобразите ее в таблицы.

CREATE TABLE publishing_houses (
publishing_house_id serial PRIMARY KEY,
name text NOT NULL
);

-- Промежуточное отношение 'editions' между отношениями 'books' и 'publishing_houses'
CREATE TABLE editions (
book_id integer REFERENCES books (book_id),
publishing_house_id integer REFERENCES publishing_houses (publishing_house_id),
edition_year integer NOT NULL,
PRIMARY KEY (book_id, publishing_house_id)
);


-- Некоторые книги могут входить в серии (например,
-- «Библиотека приключений»). Как изменится схема данных?
CREATE TABLE series (
series_id serial PRIMARY KEY,
publishing_house_id integer REFERENCES publishing_houses (publishing_house_id),
name text NOT NULL,
UNIQUE (publishing_house_id, name)
);

INSERT INTO series(name) VALUES ('Без серии');
INSERT INTO series(name) VALUES ('Библиотека приключений');
INSERT INTO series(name) VALUES ('Мир фантастики');
INSERT INTO series(name) VALUES ('Экскурс в историю');
INSERT INTO series(name) VALUES ('Научно-техническая литература');

ALTER TABLE IF EXISTS editions ADD COLUMN IF NOT EXISTS series_id integer
	NOT NULL REFERENCES series (series_id);
