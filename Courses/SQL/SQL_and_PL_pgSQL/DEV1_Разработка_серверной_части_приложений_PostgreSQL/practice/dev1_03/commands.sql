/*
Практика
1.	Создайте таблицу с одной строкой.
2.	Начните первую транзакцию и выполните запрос к таблице.
3.	Во втором сеансе удалите строку и зафиксируйте изменения.
4.	Сколько строк увидит первая транзакция, выполнив тот же запрос
повторно? Проверьте.
5.	Завершите первую транзакцию.
6.	Повторите все то же самое, но пусть теперь транзакция работает
	на уровне изоляции repeatable read:
	BEGIN ISOLATION LEVEL REPEATABLE READ;
	Объясните отличия.
*/

DROP TABLE IF EXISTS my_table;
CREATE TABLE my_table (version text);
INSERT INTO my_table VALUES ('Version one.');


-- First seance
BEGIN;
SELECT *, xmin, xmax FROM my_table;

-- Second seance
BEGIN;
DELETE FROM my_table WHERE version = 'Version one.';
COMMIT;

-- First seance
/*Because Read Committed is the default isolation level in Postgres Pro,
there're going to be no tuples as the second transaction was committed.
*/
SELECT *, xmin, xmax FROM my_table;
COMMIT;


INSERT INTO my_table VALUES ('Version one.');

-- First seance
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT *, xmin, xmax FROM my_table;

-- Second seance
BEGIN;
DELETE FROM my_table WHERE version = 'Version one.';
COMMIT;

-- First seance
/*Because the Repeatable Read isolation level only sees data committed before the transaction began,
there're going to be exactly as many tuples as there were at the beginning of the transaction.
*/
SELECT *, xmin, xmax FROM my_table;
COMMIT;