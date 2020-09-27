/*
Практика
1.	Создайте функцию onhand_qty для подсчета имеющихся
	в наличии книг. Функция принимает параметр составного типа
	books и возвращает целое число.
2.	Используйте эту функцию в представлении catalog_v
	в качестве «вычисляемого поля» onhand_qty.
3.	Проверьте, что приложение начало отображать количество
	книг.
4.	Создайте табличную функцию get_catalog для поиска книг.
	Функция принимает значения полей формы поиска «Магазина»
	(«имя автора», «название книги», «есть на складе»)
	и возвращает подходящие книги в формате catalog_v.
5.	Проверьте, что в «Магазине» начал работать поиск и просмотр.

1.
FUNCTION onhand_qty(book books) RETURNS integer

4.
FUNCTION get_catalog(
author_name text, book_title text, in_stock boolean
)
RETURNS TABLE(
book_id integer, display_name text, onhand_qty integer
)
При решении хотелось бы воспользоваться уже готовым
представлением catalog_v, просто наложив ограничения на строки. Но в
этом представлении и название книги, и авторы находятся в одном
поле, к тому же в сокращенном виде. Очевидно, что поиск автора «Лев»
по полю «Л .Н. Толстой» не даст результата.
Можно было бы повторить в функции get_catalog запрос из catalog_v, но
это дублирование кода, что плохо. Поэтому расширьте представление
catalog_v, добавив в него дополнительные поля: заголовок книги и
полный список авторов.

5.
Проверьте, что корректно обрабатываются пустые поля на форме.
Когда клиент вызывает функцию get_catalog, передает ли он в этом
случае пустые строки или неопределенные значения?
*/


psql -d bookstore

/*1.	Создайте функцию onhand_qty для подсчета имеющихся
	в наличии книг. Функция принимает параметр составного типа
	books и возвращает целое число.*/
CREATE OR REPLACE FUNCTION onhand_qty(book books) RETURNS integer
AS $$
	SELECT coalesce(sum(o.qty_change), 0)::integer
	FROM operations o WHERE o.book_id = book.book_id;
$$ STABLE LANGUAGE SQL;


/*2.	Используйте эту функцию в представлении catalog_v
	в качестве «вычисляемого поля» onhand_qty.*/
DROP VIEW catalog_v;
CREATE OR REPLACE VIEW catalog_v AS
	SELECT b.book_id, book_name(b.book_id, b.title) AS display_name,
		onhand_qty((b.book_id, b.title))
	FROM books b
	ORDER BY display_name;


/*4.	Создайте табличную функцию get_catalog для поиска книг.
	Функция принимает значения полей формы поиска «Магазина»
	(«имя автора», «название книги», «есть на складе»)
	и возвращает подходящие книги в формате catalog_v.*/
CREATE OR REPLACE FUNCTION get_authors(book books) RETURNS text
AS $$
	SELECT string_agg(a.last_name || ' ' || a.first_name || coalesce(' ' || nullif(a.middle_name,''), ''),
			', ' ORDER BY ash.seq_num)
	FROM authors a
	JOIN authorship ash
		ON a.author_id = ash.author_id
	WHERE  ash.book_id = book.book_id;
$$ STABLE LANGUAGE SQL;

DROP VIEW catalog_v;

CREATE OR REPLACE VIEW catalog_v AS
	SELECT b.book_id, b.title,
		book_name(b.book_id, b.title) AS display_name,
		onhand_qty((b.book_id, b.title)),
		get_authors((b.book_id, b.title)) AS authors
	FROM books b
	ORDER BY display_name;


CREATE OR REPLACE FUNCTION get_catalog(
	author_name text, book_title text, in_stock boolean
)
RETURNS TABLE(
	book_id integer, display_name text, onhand_qty integer
)
AS $$
	SELECT cv.book_id, 
       cv.display_name,
       cv.onhand_qty
	FROM   catalog_v cv
	WHERE  cv.title ILIKE '%'||coalesce(book_title,'')||'%'
		AND cv.authors ILIKE '%'||coalesce(author_name,'')||'%'
		AND (in_stock AND cv.onhand_qty > 0 OR in_stock IS NOT TRUE)
	ORDER BY display_name;
$$ STABLE LANGUAGE sql;
