"""Оператор [] и срезы"""

"""В python можно переопределить оператор [], определив магический метод __getitem__.
Так, например, можно создать объект, который виртуально содержит бесконечное количество повторяющихся элементов:"""


class Cycle:
    def __init__(self, lst):
        self._lst = lst

    def __getitem__(self, index):
        return self._lst[
            index % len(self._lst)
            ]


print(Cycle(['a', 'b', 'c'])[100])  # 'b'
print(Cycle(['a', 'b', 'c'])[1000])  # 'b'
print(Cycle(['a', 'b', 'c'])[1001])  # 'c'
print(Cycle(['a', 'b', 'c'])[1002], '\n')  # 'a'


"""Необычное здесь заключается в том, что оператор [] поддерживает уникальный синтаксис.
С его помощью можно получить не только [2], но и [2:10], [2:10:2], [2::2] и даже [:].
Семантика оператора такая: [start:stop:step], однако вы можете использовать его любым иным образом
для создания кастомных объектов.

Но если вызывать с помощью этого синтаксиса __getitem__, что он получит в качестве индексного параметра?
Именно для этого существуют slice-объекты."""

class Inspector:

    def __getitem__(self, index):
        print(index)

Inspector()[1]
Inspector()[1:2]
Inspector()[1:2:3]
Inspector()[:]


# Можно даже объединить синтаксисы кортежей и слайсов:
Inspector()[:, 0, :]


# slice ничего не делает, только хранит атрибуты start, stop и step.
s = slice(1, 2, 3)
print(f"type(s): {type(s)}")
print(f"s.start: {s.start}")
print(f"s.stop: {s.stop}")
print(f"s.step: {s.step}")
print(f"Inspector()[s]: {Inspector()[s]}")
