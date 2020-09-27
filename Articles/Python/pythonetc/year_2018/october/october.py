"""Подборка @pythonetc, октябрь 2018"""
# https://habr.com/company/mailru/blog/429186/

"""Устойчивость сортировки"""
print("Устойчивость сортировки")

# Стандартная сортировка в Python — устойчивая, функция sorted не меняет порядок равных объектов:
a = [2, -1, 0, 1, -2]
print(f"sorted(a, key=lambda x: x**2): {sorted(a, key=lambda x: x**2)}")

"""Функции min и max также согласованы с sorted. max работает как sorted(a, reverse=True)[0], а min – sorted(a)[0].
Это означает, что обе функции возвращают самый левый возможный ответ:"""
print(f"max([2, -2], key=lambda x: x**2): {max([2, -2], key=lambda x: x**2)}")
print(f"max([-2, 2], key=lambda x: x**2): {max([-2, 2], key=lambda x: x**2)}")
print(f"min([2, -2], key=lambda x: x**2): {min([2, -2], key=lambda x: x**2)}")
print(f"min([-2, 2], key=lambda x: x**2): {min([-2, 2], key=lambda x: x**2)}\n")



"""Кеш в аргументе по умолчанию"""
print("Кеш в аргументе по умолчанию")

"""Пожалуй, самая распространенная ошибка среди начинающих питонистов – указание изменяемого объекта
в качестве аргумента функции по умолчанию. Разделение этого объекта между вызовами функции
может привести к самым странным результатам:"""
def append_length(lst=[]):
    lst.append(len(lst))
    return lst

print(append_length([1, 2])) # [1, 2, 2]
print(append_length())       # [0]
print(append_length())       # [0, 1]
print()

# Тем не менее, такой совместный доступ будет даже полезен, если использовать объект для создания общего кэша:
def fact(x, cache={0: 1}):
    if x not in cache:
        cache[x] = x * fact(x - 1)
    return cache[x]

print(f"fact(5): {fact(5)}")

"""В данном примере мы помещаем рассчитанные значения факториала внутрь значения аргумента по умолчанию.
Такие значения даже можно извлечь:"""
print(f"fact.__defaults__: {fact.__defaults__}")

