"""https://habr.com/ru/company/mailru/blog/475684/"""

"""Если хотите итерировать сразу несколько итерируемых объектов, то можете использовать функцию zip
(не имеет никакого отношения к файловому формату ZIP):"""
from datetime import timedelta

names = [
    'Eleven. Return and Revert',
    'Wilderness',
    'The Menagerie Inside',
    'Evaporate',
]

years = [
    2010,
    2013,
    2015,
    2018,
]

durations = [
    timedelta(minutes=57, seconds=38),
    timedelta(minutes=48, seconds=5),
    timedelta(minutes=46, seconds=34),
    timedelta(minutes=43, seconds=25),
]

print('Midas Fall LPs:')
for name, year, duration in zip(names, years, durations):
    print(f'  * {name} ({year}) — {duration}')
print(f"\n\n")



"""Генератор можно остановить явным вызовом g.close(), но чаще всего сборщик мусора делает это за вас.
После вызова close, в точке, где генерирующая функция была поставлена на паузу, инициируется GeneratorExit:"""
def gen():
    try:
        yield 1
        yield 2
    finally:
        print('END')

g = gen()
print(next(g))  # prints '1'
g.close()  # prints 'END'
