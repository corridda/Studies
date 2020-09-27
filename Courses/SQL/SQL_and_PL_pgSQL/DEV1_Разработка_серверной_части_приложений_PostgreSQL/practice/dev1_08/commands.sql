/*
Практика
Влияние размера выборки на производительность.
1.	Создайте произвольную таблицу с миллионом строк в ней.
2.	Прочитайте всю таблицу с помощью курсора,
	на каждом шаге выбирая одну строку. Засеките время.
3.	Повторите п. 2, увеличив размер выборки до 10 строк.
	Как изменилось время?
4.	Повторите, увеличив размер выборки до 100 строк.
	Как изменилось время?
5.	Повторите, увеличив размер выборки до 1000 строк.
	Как изменилось время?
6.	Какие выводы можно сделать?

В SQL нет циклов, но вы можете сгенерировать файл с нужным числом
команд FETCH (например, средствами командного интерпретатора
bash или с помощью psql) и затем выполнить его.
*/


-- Создайте произвольную таблицу с миллионом строк в ней.
CREATE DATABASE bstore_interaction;
\c bstore_interaction
CREATE TABLE table_1 AS SELECT gen.num from generate_series(1, 1000000) as gen(num);
VACUUM table_1;


-- Прочитайте всю таблицу с помощью курсора,
-- на каждом шаге выбирая одну строку. Засеките время.
\q
echo 'BEGIN; DECLARE c CURSOR FOR SELECT * FROM table_1;' > /home/student/dev1/practice/dev1_08/declare.sql
echo 'CLOSE c; COMMIT;' > /home/student/dev1/practice/dev1_08/close.sql
(for i in {1..1000000}; do echo 'FETCH 1 c;'; done;) > /home/student/dev1/practice/dev1_08/fetch_1.sql

cd /home/student/dev1/practice/dev1_08/;
/usr/bin/time -f '%E' -o t cat declare.sql fetch_1.sql close.sql | psql -d bstore_interaction >/dev/null;
cat t


-- Повторите п. 2, увеличив размер выборки до 10 строк.
(for i in {1..100000}; do echo 'FETCH 10 c;'; done;) > /home/student/dev1/practice/dev1_08/fetch_10.sql
/usr/bin/time -f '%E' -o t10 cat declare.sql fetch_10.sql close.sql | psql -d bstore_interaction >/dev/null;
cat t10

-- Повторите, увеличив размер выборки до 100 строк.
(for i in {1..10000}; do echo 'FETCH 100 c;'; done;) > /home/student/dev1/practice/dev1_08/fetch_100.sql
/usr/bin/time -f '%E' -o t100 cat declare.sql fetch_100.sql close.sql | psql -d bstore_interaction >/dev/null;
cat t100

-- Повторите, увеличив размер выборки до 1000 строк.
(for i in {1..1000}; do echo 'FETCH 1000 c;'; done;) > /home/student/dev1/practice/dev1_08/fetch_1000.sql
/usr/bin/time -f '%E' -o t1000 cat declare.sql fetch_1000.sql close.sql | psql -d bstore_interaction >/dev/null;
cat t1000
