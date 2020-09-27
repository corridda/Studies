/*
Практика
1.	Создайте новую базу данных и подключитесь к ней.
2.	Создайте табличное пространство ts.
3.	Создайте таблицу t в табличном пространстве ts
	и добавьте в нее несколько строк.
4.	Вычислите объем, занимаемый базой данных, таблицей
	и табличными пространствами ts и pg_default.
5.	Перенесите таблицу в табличное пространство pg_default.
6.	Как изменился объем табличных пространств?
7.	Удалите табличное пространство ts.
*/

-- Переключиться под суперпользователя
sudo su - postgres


-- Создайте новую базу данных и подключитесь к ней.
CREATE DATABASE test;
\c test


-- Создайте табличное пространство ts.
CREATE TABLESPACE ts LOCATION '/var/lib/postgresql/ts_dir';


-- Создайте таблицу t в табличном пространстве ts
-- и добавьте в нее несколько строк.
CREATE TABLE IF NOT EXISTS t (num int) TABLESPACE ts;
INSERT INTO t SELECT * FROM generate_series(1,100000);


-- Вычислите объем, занимаемый базой данных, таблицей
-- и табличными пространствами ts и pg_default.
SELECT concat($$Database 'test' size: $$, pg_size_pretty(pg_database_size('test')));
SELECT pg_database_size('test') AS db_test_size \gset
SELECT concat($$Table 't' size (including indexes): $$, pg_size_pretty(pg_total_relation_size('t')));
SELECT pg_total_relation_size('t') AS relation_t_size \gset
SELECT concat($$Tablespace 'ts' size: $$, pg_size_pretty(pg_tablespace_size('ts')));
SELECT pg_tablespace_size('ts') AS tablespace_ts_size \gset
SELECT concat($$Tablespace 'pg_default' size: $$, pg_size_pretty(pg_tablespace_size('pg_default')));
SELECT pg_tablespace_size('pg_default') AS tablespace_pg_default_size \gset
SELECT (:'db_test_size')::bigint + (:'relation_t_size')::bigint + (:'tablespace_ts_size')::bigint + 
	(:'tablespace_pg_default_size')::bigint AS total_size \gset
SELECT concat($$Total size: $$, pg_size_pretty((:'total_size')::bigint));


-- Перенесите таблицу в табличное пространство pg_default.
-- Текущее табличное пространство
\d+ t
ALTER TABLE IF EXISTS t SET TABLESPACE pg_default;
\d+ t


-- Как изменился объем табличных пространств?
SELECT concat($$Tablespace 'ts' size: $$, pg_size_pretty(pg_tablespace_size('ts')));
SELECT concat($$Tablespace 'pg_default' size: $$, pg_size_pretty(pg_tablespace_size('pg_default')));


-- Удалите табличное пространство ts.
DROP TABLESPACE ts;
-- Список существующих табличных пространств
\db

DROP TABLE t;
\c postgres
DROP DATABASE test;