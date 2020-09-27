/*Нарастающий итог в SQL
https://habr.com/ru/post/474458/

The following example is relevant for PostgreSQL
*/

-- создание таблиц и наполнение их данными --
-- простейший случай
create table test_simple (dt date null,
                          val int null
                         ); 
-- используем формат дат своей СУБД (или меняем настройки, напр. через NLS_DATE_FORMAT в Oracle)
insert into test_simple (dt, val) values ('2019-11-01'::date, 6);
insert into test_simple (dt, val) values ('2019-11-02'::date, 3);
insert into test_simple (dt, val) values ('2019-11-03'::date, 3);
insert into test_simple (dt, val) values ('2019-11-04'::date, 4);
insert into test_simple (dt, val) values ('2019-11-05'::date, 2);
insert into test_simple (dt, val) values ('2019-11-06'::date, 4);
insert into test_simple (dt, val) values ('2019-11-07'::date, 8);
insert into test_simple (dt, val) values ('2019-11-08'::date, 0);
insert into test_simple (dt, val) values ('2019-11-09'::date, 6);
insert into test_simple (dt, val) values ('2019-11-10'::date, 0);
insert into test_simple (dt, val) values ('2019-11-11'::date, 8);
insert into test_simple (dt, val) values ('2019-11-12'::date, 8);
insert into test_simple (dt, val) values ('2019-11-13'::date, 0);
insert into test_simple (dt, val) values ('2019-11-14'::date, 2);
insert into test_simple (dt, val) values ('2019-11-15'::date, 8);
insert into test_simple (dt, val) values ('2019-11-16'::date, 7);

-- случай с группами
create table test_groups (grp varchar null, -- varchar2(1) in Oracle
                          dt date null,
                          val int null
                          );
-- используем формат дат своей СУБД (или меняем настройки, напр. через NLS_DATE_FORMAT в Oracle)
insert into test_groups (grp, dt, val) values ('a', '2019-11-06'::date, 1);
insert into test_groups (grp, dt, val) values ('a', '2019-11-07'::date, 3);
insert into test_groups (grp, dt, val) values ('a', '2019-11-08'::date, 4);
insert into test_groups (grp, dt, val) values ('a', '2019-11-09'::date, 1);
insert into test_groups (grp, dt, val) values ('a', '2019-11-10'::date, 7);
insert into test_groups (grp, dt, val) values ('b', '2019-11-06'::date, 9);
insert into test_groups (grp, dt, val) values ('b', '2019-11-07'::date, 10);
insert into test_groups (grp, dt, val) values ('b', '2019-11-08'::date, 9);
insert into test_groups (grp, dt, val) values ('b', '2019-11-09'::date, 1);
insert into test_groups (grp, dt, val) values ('b', '2019-11-10'::date, 10);
insert into test_groups (grp, dt, val) values ('c', '2019-11-06'::date, 4);
insert into test_groups (grp, dt, val) values ('c', '2019-11-07'::date, 10);
insert into test_groups (grp, dt, val) values ('c', '2019-11-08'::date, 9);
insert into test_groups (grp, dt, val) values ('c', '2019-11-09'::date, 4);
insert into test_groups (grp, dt, val) values ('c', '2019-11-10'::date, 4);

-- проверяем данные --
select * from test_simple order by dt;
select * from test_groups order by grp, dt;



-- 1. Оконные функции
/*Оконные функции – вероятно, самый простой способ.
В базовом случае (таблица без групп) мы рассматриваем данные,
отсортированные по дате:*/
select s.*,
       coalesce(sum(s.val) over (order by s.dt 
                rows between unbounded preceding and current row), 0) as total
from test_simple s
order by s.dt;

/*В случае нарастающего итога по группам (поле grp) нам требуется только одна небольшая правка.
Теперь мы рассматриваем данные как разделённые на «окна» по признаку группы:*/
select tg.*,
       coalesce(sum(tg.val) over (partition by tg.grp order by tg.dt
                rows between unbounded preceding and current row), 
                0) as total
from test_groups tg
order by tg.grp, tg.dt;


-- 2. Подзапрос
/*Такой подзапрос должен считать сумму значений с датой до текущей (и включая текущую):*/
--dt_row <= dt_currentrow
select s.*,
       (select coalesce(sum(t2.val), 0)
	from test_simple t2
	where t2.dt <= s.dt) as total
from test_simple s
order by s.dt;

/*Чуть более эффективным будет решение, в котором подзапрос считает итог до текущей даты
(но не включая её), а затем суммирует его со значением в строке:*/
select s.*,
       s.val + (select coalesce(sum(t2.val), 0)
	        from test_simple t2
	        where t2.dt < s.dt) as total
from test_simple s
order by s.dt;

/*В случае нарастающего итога по нескольким группам
нам необходимо использовать коррелированный подзапрос.
Условие "g.grp = t2.grp" проверяет строки на вхождение в группу
(что, в принципе, сходно с работой partition by grp в оконных функциях).*/
select g.*,
	(select coalesce(sum(t2.val), 0) as total
	 from test_groups t2
	 where g.grp = t2.grp
	          and t2.dt <= g.dt) as total
from test_groups g
order by g.grp, g.dt;


-- 3. Внутреннее соединение
/*Поскольку подзапросы и джойны взаимозаменяемы, мы легко можем заменить одно на другое.
Для этого необходимо использовать Self Join, соединив два экземпляра одной и той же таблицы.
условие фильтрации в подзапросе "t2.dt <= s.dt" стало условием соединения.
Кроме того, чтобы использовать агрегирующую функцию sum() нам необходима
группировка по дате и значению group by s.dt, s.val.*/
select s.*, 
       coalesce(sum(t2.val), 0) as total
from test_simple s
inner join test_simple t2
	 on t2.dt <= s.dt
group by s.dt, s.val
order by s.dt;

-- Точно также можно сделать для случая с разными группами grp:
select g.*, 
       coalesce(sum(t2.val), 0) as total
from test_groups g
inner join test_groups t2
	on g.grp = t2.grp
		and t2.dt <= g.dt
group by g.grp, 
	 g.dt, 
	 g.val
order by g.grp, 
	 g.dt;


-- 4. Декартово произведение
select s.*, 
       coalesce(sum(t2.val), 0) as total
from test_simple s
cross join test_simple t2
where t2.dt <= s.dt
group by s.dt, 
	 s.val
order by s.dt;

-- для случая с группами:
select g.*, 
       coalesce(sum(t2.val), 0) as total
from test_groups g
cross join test_groups t2
where g.grp = t2.grp
	and t2.dt <= g.dt
group by g.grp, 
	 g.dt, 
	 g.val
order by g.grp, 
	 g.dt;


-- 5. Рекурсивный запрос
/*Один из более специфических подходов – это рекурсивный запрос в common table expression.
Для этого нам необходим «якорь» – запрос, возвращающий самую первую строку.
Затем к «якорю» с помощью union all присоединяются результаты рекурсивного запроса.
Для этого можно опереться на поле даты dt, прибавляя у нему по одному дню:*/
with recursive cte (dt, val, total)
as
   (select dt, val, val as total
    from test_simple
    where dt = (select min(dt) from test_simple)
			
    union all
			
    select r.dt, r.val, cte.total + r.val
    from cte
    inner join test_simple r
    	on r.dt = cte.dt + '1 day'::interval
    )
select dt, val, total 
from cte
order by dt;

-- Решение для случая с группами будет ненамного сложнее:
with recursive cte (dt, grp, val, total)
as
   (select g.dt, g.grp, g.val, g.val as total
    from test_groups g
    where g.dt = (select min(dt) from test_groups where grp = g.grp)
			
    union all
			
    select r.dt, r.grp, r.val, cte.total + r.val 
    from cte
    inner join test_groups r
    	on r.dt = cte.dt + '1 day'::interval
		and cte.grp = r.grp
    )
select dt, grp, val, total 
from cte
order by grp, dt;


-- 6. Рекурсивный запрос с функцией row_number()
/*Предыдущее решение опиралось на непрерывность поля даты dt с последовательным приростом на 1 день.
Мы избежать этого, используя оконную функцию row_number(), которая нумерует строки.
Для рекурсивного запроса с row_number() нам понадобится два СТЕ. В первом мы только нумеруем строки.
и если номер строки уже есть в таблице, то можно без него обойтись.*/
with recursive cte1 (dt, val, rn)
as (select dt,
           val,
	   row_number() over (order by dt) as rn
	from test_simple),
cte2 (dt, val, rn, total)
as
   (select dt, val, rn, val as total
    from cte1
    where rn = 1
			
    union all
			
    select cte1.dt, cte1.val, cte1.rn, cte2.total + cte1.val
    from cte2
    inner join cte1
    	on cte1.rn = cte2.rn + 1
    )
select dt, val, total 
from cte2
order by dt;

-- … или для случая с группами:
with recursive cte1 (dt, grp, val, rn)
as (select dt, grp, val,
	   row_number() over (partition by grp order by dt) as rn
   from test_groups),
cte2 (dt, grp, val, rn, total)
as
   (select dt, grp, val, rn, val as total
    from cte1
    where rn = 1
			
    union all
			
    select cte1.dt, cte1.grp, cte1.val, cte1.rn, cte2.total + cte1.val
    from cte2
    inner join cte1
    	on cte1.grp = cte2.grp
		    and cte1.rn = cte2.rn + 1
    )
select dt, grp, val, total 
from cte2
order by grp, dt;


-- 7. Оператор CROSS APPLY / LATERAL
/*Один из самых экзотических способов расчёта нарастающего итога –
это использование оператора CROSS APPLY (SQL Server, SQL Server)
или эквивалентного ему LATERAL (MySQL, PostgreSQL).
Функционально использование CROSS APPLY или LATERAL идентично подзапросу:
мы присоединяем к основному запросу результат вычисления:*/
select s.*,
       t2.total
from test_simple s,
lateral (select coalesce(sum(t2.val), 0) as total
             from test_simple t2
	     where t2.dt <= s.dt
) t2
order by s.dt;

-- Похожим будет и решение для случая с группами:
select g.*,
       t2.total
from test_groups g,
lateral (select coalesce(sum(t2.val), 0) as total
             from test_groups t2
	     where g.grp = t2.grp
	            and t2.dt <= g.dt
) t2
order by g.grp,
         g.dt;

drop table test_simple;
drop table test_groups;
