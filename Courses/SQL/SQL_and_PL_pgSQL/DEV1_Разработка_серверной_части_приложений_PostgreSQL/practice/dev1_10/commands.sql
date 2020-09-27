/*
Практика
1.	Напишите функцию, переводящую строку, содержащую
	число в шестнадцатеричной системе, в обычное целое число.
	Например: convert('FF') → 255
2.	Добавьте в функцию второй необязательный параметр —
	основание системы счисления (по умолчанию — 16).
	Например: convert('0110',2) → 6
3.	Табличная функция generate_series не работает со
	строковыми типами. Предложите свою функцию для
	генерации последовательностей строк из заглавных
	английских букв.

1. Например:
	convert('FF') → 255
	Для решения пригодятся: табличная функция regexp_split_to_table,
	функции uppper и reverse, конструкция WITH ORDINALITY.
	Другое решение возможно с помощью рекурсивного запроса.
	Проверить реализацию можно, используя шестнадцатеричные
	константы: SELECT X'FF'::integer;
2. Например:
	convert('0110',2) → 6
3. Считайте, что на вход подаются строки равной длины. Например:
	generate_series('AA','ZZ') →
	→ 'AA'
	'AB'
	'AC'
	...
	'ZY'
	'ZZ'
*/


/*1.	Напишите функцию, переводящую строку, содержащую
	число в шестнадцатеричной системе, в обычное целое число.
	Например: convert('FF') → 255*/
CREATE OR REPLACE FUNCTION convert_16_to_10(IN hex text, OUT out_num bigint)
AS $$
	WITH t1(sign, power) AS(
		SELECT * FROM  regexp_split_to_table(reverse(upper(hex)),'') with ordinality AS t(sign, power)
	),
	t2(sign, power, frac) AS(
		SELECT t1.sign, (t1.power - 1) AS power , 	
			CASE 	WHEN t1.sign ~ '[A-F]' THEN ascii(t1.sign) - 55
					WHEN ascii(t1.sign) BETWEEN 48 AND 57 THEN t1.sign::integer
					ELSE null
			END AS frac
		FROM t1
	),
	t3(sign, power, frac, val) AS (
		SELECT t2.*, (t2.frac * (16^(t2.power))) AS val FROM t2
	)
	SELECT CASE WHEN (SELECT COUNT(*) <> COUNT(t3.frac) FROM t3) THEN null
				ELSE sum(t3.val)::bigint
           END
    FROM t3
$$ IMMUTABLE LANGUAGE SQL;



/*2.	Добавьте в функцию второй необязательный параметр —
	основание системы счисления (по умолчанию — 16).*/	
CREATE OR REPLACE FUNCTION convert_num_to_num10(IN num text, IN base integer DEFAULT 16, OUT out_num bigint)
AS $$
	WITH t1(sign, power) AS(
		SELECT * FROM  regexp_split_to_table(reverse(upper(num)),'') with ordinality AS t(sign, power)
	),
	t2(sign, power, mult) AS(
		SELECT t1.sign, (t1.power - 1) AS power , 	
			CASE 	WHEN t1.sign ~ '[A-Z]' THEN ascii(t1.sign) - 55
					WHEN ascii(t1.sign) BETWEEN 48 AND 57 THEN t1.sign::integer
					ELSE null
			END AS mult
		FROM t1
	),
	t3(sign, power, mult, val) AS (
		SELECT t2.*, (t2.mult * (base^(t2.power))) AS val FROM t2
	)
	SELECT CASE WHEN (SELECT COUNT(*) <> COUNT(t3.mult) FROM t3) THEN null
				ELSE sum(t3.val)::bigint
           END
    FROM t3
$$ IMMUTABLE LANGUAGE SQL;



/*3.	Табличная функция generate_series не работает со
	строковыми типами. Предложите свою функцию для
	генерации последовательностей строк из заглавных
	английских букв.*/

-- turn text to number
CREATE OR REPLACE FUNCTION text_to_number(IN txt text, OUT out_num int)
AS $$
	WITH t1(sign, power) AS(
		SELECT * FROM  regexp_split_to_table(reverse(upper(txt)),'') with ordinality AS t(sign, power)
	),
	t2(sign, power, mult) AS(
		SELECT t1.sign, (t1.power - 1) AS power , 	
			CASE 	WHEN t1.sign ~ '[A-Z]' THEN ascii(t1.sign) - 65
					ELSE null
			END AS mult
		FROM t1
	),
	t3(sign, power, mult, val) AS (
		SELECT t2.*, (t2.mult * (26^(t2.power))) AS val FROM t2
	)
	SELECT CASE WHEN (SELECT COUNT(*) <> COUNT(t3.mult) FROM t3) THEN null
				ELSE sum(t3.val)::int
           END
    FROM t3
$$ IMMUTABLE LANGUAGE SQL;

-- turn number to text
CREATE OR REPLACE FUNCTION number_to_text(IN numb int, IN num_of_digits int, OUT txt text)
AS $$
	WITH RECURSIVE t1(num, txt, digit) AS (
		SELECT numb / 26, chr( numb % 26 + ascii('A') )::text, 1
		UNION ALL
		SELECT t1.num / 26, concat(chr( t1.num % 26 + ascii('A') ), t1.txt), t1.digit + 1
		FROM t1
		WHERE t1.digit < num_of_digits
	)
	SELECT t1.txt FROM t1 WHERE t1.digit = num_of_digits;
$$ IMMUTABLE LANGUAGE SQL;

-- generate series
CREATE OR REPLACE FUNCTION generate_letters(IN start text, IN finish text)
RETURNS TABLE(txt text) AS $$
	SELECT number_to_text(s.num, length(start))
	FROM generate_series(text_to_number(start), text_to_number(finish)) s(num);
$$ IMMUTABLE LANGUAGE SQL;
