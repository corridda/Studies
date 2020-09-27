/*
Практика
1. Установите в postgresql.conf для параметра work_mem
значение 8 мегабайт.
2. Обновите конфигурацию и проверьте, что изменения
вступили в силу.
3. Запишите в файл ddl.sql команду CREATE TABLE на
создание любой таблицы.
4. Запишите в файл populate.sql команды на вставку строк в эту
таблицу.
5. Войдите в psql, выполните оба скрипта и проверьте, что
таблица создалась и в ней появились записи.
6. Найдите в журнале сервера все строки за сегодняшний день.
*/

\! echo 'CREATE TABLE my_table (a int, b text);' > /home/student/Documents/ddl.sql
\! echo "INSERT INTO my_table VALUES (1, 'one'), (2, 'two'), (3, 'three');" > /home/student/Documents/populate.sql
DROP TABLE IF EXISTS my_table;
\i /home/student/Documents/ddl.sql
\i /home/student/Documents/populate.sql
SELECT * FROM my_table;
\! sed -n '/^2019-11-07/,$p' /var/log/postgresql/postgresql-9.6-main.log
DROP TABLE IF EXISTS my_table;
