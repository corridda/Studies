/*��������� ��������� �� ������� ������� �������� ��������� ����������: ����: �������, ��� ������
����� � 5 ���� �����, ��� ��, ����������� ��� ��� ���� � ���� ������������ ������*/

-- �������
SELECT DATEPART(YEAR, CURRENT_TIMESTAMP) AS YEAR,
DATEPART(MONTH, CURRENT_TIMESTAMP) AS MONTH,
DATEPART(DAY, CURRENT_TIMESTAMP) AS DAY,
DATEPART(HOUR, CURRENT_TIMESTAMP) AS HOUR,
DATEPART(MINUTE, CURRENT_TIMESTAMP) AS MINUTE,
DATEPART(SECOND, CURRENT_TIMESTAMP) AS SECOND

-- ��� ������ �����
SELECT DATEPART(YEAR, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS YEAR,
DATEPART(MONTH, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS MONTH,
DATEPART(DAY, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS DAY,
DATEPART(HOUR, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS HOUR,
DATEPART(MINUTE, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS MINUTE,
DATEPART(SECOND, DATEADD(MONTH, -3, CURRENT_TIMESTAMP)) AS SECOND

-- 5 ���� �����
SELECT DATEPART(YEAR, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS YEAR,
DATEPART(MONTH, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS MONTH,
DATEPART(DAY, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS DAY,
DATEPART(HOUR, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS HOUR,
DATEPART(MINUTE, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS MINUTE,
DATEPART(SECOND, DATEADD(DAY, -5, CURRENT_TIMESTAMP)) AS SECOND


/*��������� ��������� �� ������� ������� �������� ��������� ����������:
- �������� ������� ���� �������� ������������, ��� ���� ������������ �� ��������� �����.
����������� ��������� ���������.
- �������� ������� �� ������� �������, �������� ��� ������������� �������� ����������
���������� ������������ �� ������ "Undefined"*/

USE BookingsDB;
GO

SELECT * FROM [dbo].[bookings]
WHERE [book_date] >= DATEADD(MONTH, -1, (SELECT MAX([book_date]) FROM [dbo].[bookings]))

UPDATE [dbo].[tickets]
SET [contact_data] = NULL
WHERE [passenger_id] IN ('3889 683019', '5118 216478', '2963 652080')

SELECT COUNT(*) FROM [dbo].[tickets]
WHERE [contact_data] IS NULL

SELECT TOP(30) [ticket_no], [book_ref], [passenger_id], [passenger_name],
	IIF([contact_data] IS NULL, 'Undefined', [contact_data]) AS [contact_data]
FROM [dbo].[tickets]