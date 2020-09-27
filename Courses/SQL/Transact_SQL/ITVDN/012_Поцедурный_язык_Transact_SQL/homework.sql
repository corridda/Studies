/*«адание
—оздайте цикл, который будет прерыватьс€, как только его целочисленный счетчик будет кратен 3, 4, 5.*/

DECLARE @iterator int = 0;

WHILE @iterator < 10
BEGIN
	SET @iterator = @iterator + 1;
	IF @iterator % 3 = 0
		BEGIN
			PRINT '3 is an aliquot part of '  + CAST(@iterator as varchar);
			CONTINUE
		END
	ELSE IF @iterator % 4 = 0
		BEGIN
			PRINT '4 is an aliquot part of '  + CAST(@iterator as varchar);
			CONTINUE
		END
	ELSE IF @iterator % 5 = 0
		BEGIN
			PRINT '5 is an aliquot part of '  + CAST(@iterator as varchar);
			BREAK
		END
	ELSE
		BEGIN
			PRINT @iterator;
		END
END;
GO


/*«адание 1
Ќапишите алгоритм, определ€ющий €вл€етс€ ли значение некоторой целочисленной переменной
простым числом.*/
PRINT '';
PRINT '---Even number---';
DECLARE @num int = 2, @iterator int;

WHILE @num < 21
BEGIN
	SET @iterator = 2;
	WHILE @iterator <= (@num / 2)
	BEGIN
		IF @num % @iterator = 0
			BREAK;
		ELSE
			SET @iterator = @iterator + 1;
	END
	IF @num % @iterator <> 0
		PRINT CAST(@num as varchar) + ' is prime';
	SET @num = @num + 1;
END;
GO
