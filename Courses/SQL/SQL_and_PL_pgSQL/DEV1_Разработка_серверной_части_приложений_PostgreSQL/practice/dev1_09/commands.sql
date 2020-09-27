/*
Практика
Обратите внимание на категории изменчивости функций.
1.	Напишите функцию, выдающую случайное время,
	равномерно распределенное в указанном отрезке.
	Начало отрезка задается временной отметкой (timestamptz),
	конец — либо временной отметкой, либо интервалом (interval).
2.	В таблице хранятся номера автомобилей, введенные кое-как:
	встречаются как латинские, так и русские буквы в любом
	регистре; между буквами и цифрами могут быть пробелы.
	Считая, что формат номера «буква три-цифры две-буквы»,
	напишите функцию, выдающую число уникальных номеров.
	Например, «К 123 ХМ» и «k123xm» считаются равными.
3.	Напишите функцию, находящую корни квадратного уравнения.


п.2. Сначала напишите функцию «нормализации» номера, то есть
приводящую номер к какому-нибудь стандартному виду. Например, без
пробелов и только заглавными латинскими буквами.
В номерах используются 12 русских букв, имеющих латинские аналоги
аналогичного начертания, а именно: АВЕКМНОРСТУХ.

п.3. Для уравнения y = ax2 + bx + c:
дискриминант D = b2 – 4ac.
● при D > 0 два корня x1,2 = (–b ± √D) / 2a
● при D = 0 один корень x = –b / 2a (в качестве x2 можно вернуть null)
● при D < 0 корней нет (оба корня null).
*/


/*Напишите функцию, выдающую случайное время,
равномерно распределенное в указанном отрезке.
Начало отрезка задается временной отметкой (timestamptz),
конец — либо временной отметкой, либо интервалом (interval).*/

-- конец — временная отметка
CREATE OR REPLACE FUNCTION randomTime(IN begin_val timestamptz DEFAULT LOCALTIMESTAMP,
	IN end_val timestamptz DEFAULT LOCALTIMESTAMP + '1 day'::interval,
	OUT randomTS timestamptz)
	LANGUAGE SQL
	AS $$
		WITH subq_1 AS(
			SELECT extract(epoch from begin_val) AS begin_val
		),
		subq_2 AS(
			SELECT extract(epoch from end_val) AS end_val
		),
		subq_3 AS(
			SELECT (random()*(subq_2.end_val - subq_1.begin_val) + subq_1.begin_val) AS rand FROM subq_1, subq_2
		)
		SELECT to_timestamp(rand) FROM subq_3;
	$$;

-- конец — интервал
CREATE OR REPLACE FUNCTION randomTime(IN begin_val timestamptz DEFAULT LOCALTIMESTAMP,
	IN end_val_interval interval DEFAULT '1 day'::interval,
	OUT randomTS timestamptz)
	LANGUAGE SQL
	AS 	$$
		SELECT randomTime(begin_val, begin_val + end_val_interval);
	$$;
	


-- Напишите функцию, выдающую число уникальных номеров.

CREATE TABLE cars(
    id serial PRIMARY KEY,
    regnum text
);

INSERT INTO cars(regnum) VALUES ('К 123 ХМ'), ('k123xm'), ('A 098BC');


CREATE OR REPLACE FUNCTION normalize(INOUT regnum text)
	IMMUTABLELANGUAGE SQL
	AS $$
		SELECT upper(translate(regnum, 'АВЕКМНОРСТУХ ', 'ABEKMHOPCTYX'));
	$$;

CREATE OR REPLACE FUNCTION unique_nums() RETURNS bigint
	STABLE LANGUAGE SQL
	AS $$
		SELECT count(DISTINCT normalize(regnum)) FROM cars;
	$$;



-- Напишите функцию, находящую корни квадратного уравнения.
CREATE OR REPLACE FUNCTION roots(IN a real, IN b real DEFAULT 0, IN c real DEFAULT 0, OUT root1 real, OUT root2 real)
IMMUTABLE LANGUAGE SQL
AS $$
	WITH discr AS(
		SELECT (b^2 - 4*a*c) AS d
	)
	SELECT 	CASE WHEN d < 0 THEN (null, null)
				WHEN d = 0 THEN (-b / (2*a), null)
				ELSE ((-b + sqrt(d)) / (2*a), (-b - sqrt(d)) / (2*a))
			END
			FROM discr
$$;
