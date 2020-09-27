/*
Практика
Здесь и далее все практические задания, связанные
с приложением, выполняются в базе данных bookstore.

1.	Создайте представление authors_v для авторов книг.
2.	Создайте представление catalog_v для каталога книг.
3.	Создайте представление operations_v для операций.
4.	Проверьте, что приложение стало показывать данные
	на вкладках «Книги», «Авторы» и «Каталог».

1. Authors_v:
	author_id		integer
	display_name	text 	— фамилия, имя и отчество
Что будет показывать представление, если отчество будет не
определено (NULL)?
Не будет ли выводиться лишний пробел, если отчество пустое ('')?

2. Catalog_v:
	book_id			integer
	display_name	text	 — название книги

3. Operations_v:
	book_id			integer
	op_type			text	 — тип операции (поступление или покупка)
	qty_change		integer
	date_created	date
*/


psql -d bookstore


-- Создайте представление authors_v для авторов книг.
CREATE VIEW authors_v AS
WITH subq AS (
	SELECT 	author_id,
			last_name,
			first_name,
			(CASE WHEN middle_name IS NULL THEN '' ELSE middle_name END) AS middle_name
	FROM authors
)	
SELECT author_id, 	(CASE WHEN middle_name = '' THEN
					concat(last_name, ' ', first_name)
					ELSE concat(last_name, ' ', first_name, ' ', middle_name)
					END) AS display_name
FROM subq;


-- Создайте представление catalog_v для каталога книг.
CREATE VIEW catalog_v AS
	SELECT book_id, title AS display_name FROM books;


-- Создайте представление operations_v для операций.
CREATE VIEW operations_v AS
SELECT 	book_id,
		(CASE WHEN qty_change > 0 THEN 'поступление'
		ELSE 'покупка' END) AS op_type,
		abs(qty_change),
		to_char(date_created, 'DD.MM.YYYY') AS date_created
FROM operations;
