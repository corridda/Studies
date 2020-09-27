/*
Практика
1.	Создайте функцию author_name для формирования имени
	автора.
	Функция принимает три параметра (фамилия, имя, отчество)
	и возвращает строку с фамилией и инициалами.
2.	Используйте эту функцию в представлении authors_v.
3.	Создайте функцию book_name для формирования названия
	книги.
	Функция принимает два параметра (идентификатор книги и
	заголовок) и возвращает строку, составленную из заголовка и
	списка авторов в порядке seq_num. Имя каждого автора
	формируется функцией author_name.
4.	Используйте эту функцию в представлении catalog_v.
5.	Проверьте изменения в приложении.

1.
FUNCTION author_name(
	last_name text, first_name text, middle_name text
)
RETURNS text

Например:
author_name('Толстой','Лев','Николаевич') → 'Толстой Л. Н.'

3.
FUNCTION book_name(book_id integer, title text)
RETURNS text

Например:
book_name(3,'Трудно быть богом') →
→ 'Трудно быть богом. Стругацкий А. Н., Стругацкий Б. Н.'
*/


psql -d bookstore

/*Создайте функцию author_name для формирования имени автора.
Функция принимает три параметра (фамилия, имя, отчество)
и возвращает строку с фамилией и инициалами.*/
CREATE OR REPLACE FUNCTION author_name(
	last_name text, first_name text, middle_name text)
RETURNS text
IMMUTABLE LANGUAGE SQL
AS $$
	SELECT concat(last_name, ' ',
		upper(substring(first_name from 1 for 1)), '.',
		(CASE WHEN middle_name IS NULL THEN '' ELSE concat(' ', upper(substring(middle_name from 1 for 1)), '.') END))
$$;


-- Используйте эту функцию в представлении authors_v.
CREATE OR REPLACE VIEW authors_v
	AS SELECT author_id, author_name(last_name, first_name, middle_name) AS display_name FROM authors;


/*Создайте функцию book_name для формирования названия книги.
Функция принимает два параметра (идентификатор книги и
заголовок) и возвращает строку, составленную из заголовка и
списка авторов в порядке seq_num. Имя каждого автора
формируется функцией author_name.*/

CREATE OR REPLACE FUNCTION book_name(book_id integer, title text)
RETURNS text
IMMUTABLE LANGUAGE SQL
AS $$
	SELECT concat(title, '. ', string_agg(author_name(a.last_name, a.first_name, a.middle_name), ', ' ORDER BY a_s.seq_num))
	FROM authorship a_s
		JOIN authors a
	ON a.author_id = a_s.author_id
	WHERE a_s.book_id = book_name.book_id
$$;


-- Используйте эту функцию в представлении catalog_v.
DROP VIEW IF EXISTS catalog_v;
CREATE VIEW catalog_v AS
SELECT b.book_id, book_name(b.book_id, b.title) AS display_name FROM books b;
