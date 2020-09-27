/*
Практика
1.	Создайте новую базу данных и подключитесь к ней.
2.	Создайте схему, названную так же, как и пользователь.
3.	Создайте схему app.
4.	Создайте несколько таблиц в обоих схемах.
5.	Получите в psql описание созданных схем и список
	всех таблиц в них.
6.	Установите путь поиска так, чтобы при подключении к БД
	таблицы из обоих схем были доступны по неквалифицированному
	имени; приоритет должна иметь «пользовательская» схема.
7.	Проверьте правильность настройки.
*/


-- Создайте новую базу данных и подключитесь к ней.
CREATE DATABASE test;
\c test;


-- Создайте схему, названную так же, как и пользователь.
CREATE SCHEMA IF NOT EXISTS AUTHORIZATION CURRENT_USER;


-- Создайте схему app.
CREATE SCHEMA IF NOT EXISTS app;


-- Создайте несколько таблиц в обоих схемах.
SELECT CURRENT_USER AS cuser \gset
-- Установить первой в search_path
SET search_path = :'cuser', app, public;
-- таблицы в схеме, названной так же, как и пользователь
CREATE TABLE IF NOT EXISTS table_1(a int, b int);
CREATE TABLE IF NOT EXISTS table_2(c int, d int);
CREATE TABLE IF NOT EXISTS table_3(e int, f int);
-- таблицы в схеме 'app'
CREATE TABLE IF NOT EXISTS app.table_1(a int, b int);
CREATE TABLE IF NOT EXISTS app.table_2(c int, d int);
CREATE TABLE IF NOT EXISTS app.table_3(e int, f int);


-- Получите в psql описание созданных схем и список всех таблиц в них.
SELECT n.nspname AS "Name",
  pg_catalog.pg_get_userbyid(n.nspowner) AS "Owner",
  pg_catalog.array_to_string(n.nspacl, E'\n') AS "Access privileges",
  pg_catalog.obj_description(n.oid, 'pg_namespace') AS "Description"
FROM pg_catalog.pg_namespace n
WHERE n.nspname = :'cuser' OR n.nspname = 'app'
ORDER BY 1;

-- список  всех таблиц в схеме, названной так же, как и пользователь
\dt
-- список  всех таблиц в схеме 'app'
\dt app.*


-- Установите путь поиска так, чтобы при подключении к БД
-- таблицы из обоих схем были доступны по неквалифицированному
-- имени; приоритет должна иметь «пользовательская» схема.
ALTER DATABASE test SET search_path = :'cuser', app, public;


--Проверьте правильность настройки.
\! sudo pg_ctlcluster 9.6 main restart
show search_path;



