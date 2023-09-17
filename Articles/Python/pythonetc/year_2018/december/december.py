"""Подборка @pythonetc, декабрь 2018
https://habr.com/ru/company/mailru/blog/436322/"""

import gc
import re
from datetime import datetime
from contextlib import ExitStack


"""Множественные контексты"""

# Иногда бывает нужно запустить какой-то блок кода в нескольких менеджерах контекста:
with open('f') as f:
    with open('g') as g:
        with open('h') as h:
            pass

# Со времён python 2.7 и 3.1 это можно сделать с помощью одного выражения:
o = open
with o('f') as f, o('g') as g, o('h') as h:
    pass

"""Если вы работаете с неопределённым количеством менеджеров контекста, то лучше выбрать более
продвинутые инструменты. contextlib.ExitStack позволяет в любое время входить в любое количество контекстов
и гарантирует выход из них по окончании исполнения:"""
with ExitStack() as stack:
    f = stack.enter_context(o('f'))
    g = stack.enter_context(o('g'))
    filenames = ['a', 'b']
    other = [
        stack.enter_context(o(filename))
        for filename in filenames
    ]




"""Объекты в памяти интерпретатора"""

"""Ко всем объектам, которые в данный момент находятся в памяти интерпретатора, можно получить доступ
с помощью gc.get_objects():"""

# run in console
class A:
    def __init__(self, x):
        self._x = x

    def __repr__(self):
        class_name = type(self).__name__
        x = self._x
        return f'{class_name}({x!r})'


print(A(1))
print(A(2))
print(A(3))
print([x for x in gc.get_objects() if isinstance(x, A)])
print()




"""Символы-цифры"""

"""0 1 2 3 4 5 6 7 8 9 — это не единственные символы, считающиеся цифрами. python соблюдает правила Unicode
и считает цифрами несколько сотен символов. Полный список здесь:
http://www.fileformat.info/info/unicode/category/Nd/list.htm

Это имеет значение для функций вроде int, unicode.isdecimal и даже re.match:"""

print(f"int('௯'): {int('௯')}")
print(f"'٢'.isdecimal(): {'٢'.isdecimal()}")
print(f"int('٩') + int('٦'): {int('٩') + int('٦')}")
temp = '\d'
print(f"bool(re.match('\d', '౫')): {bool(re.match(temp, '౫'))}\n")




"""Полночь по UTC"""

# До Pyhon 3.5 объекты datetime.time() считались ложными, если они представляли полночь по UTC.
print(f"datetime(2018, 1, 1).time(): {datetime(2018, 1, 1).time()}")
print(f"bool(datetime(2018, 1, 1).time()): {bool(datetime(2018, 1, 1).time())}")
print(f"datetime(2018, 1, 1, 13, 12, 11).time(): {datetime(2018, 1, 1, 13, 12, 11).time()}")
print(f"bool(datetime(2018, 1, 1, 13, 12, 11).time()): {bool(datetime(2018, 1, 1, 13, 12, 11).time())}")

"""Это может приводить к неочевидным багам. В следующем примере if not может не выполниться не потому, что create_time
является None, а потому что это полночь. Обойти этот баг можно с помощью явной проверки на None:
if created_time is None."""
def create(created_time=None) -> None:
    if not created_time:
        created_time = datetime.now().time()



"""Асинхронная работа в ФС"""

"""python не поддерживает асинхронные операции с файлами. Чтобы сделать их неблокирующими,
приходится использовать треды.

Для асинхронного исполнения кода в потоке нужно использовать метод loop.run_in_executor.

За вас это может сделать сторонний модуль aiofiles, предоставляющий удобный и простой интерфейс:

async with aiofiles.open('filename', mode='r') as f:
    contents = await f.read()"""