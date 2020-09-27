"""Ускорение кода с использованием Cython

Начнём с создания Python-бенчмарка. Это будет цикл for, в котором выполняется вычисление факториала числа.
Соответствующий код на чистом Python будет выглядеть так:
"""

# def test(x):
#     y = 1
#     for i in range(1, x+1):
#         y *= i
#     return y

"""Cython-эквивалент этой функции очень похож на её исходный вариант.
Соответствующий код нужно поместить в файл с расширением .pyx.
Единственное изменение, которое нужно внести в код, заключается в добавлении в него сведений о типах переменных
и функции:"""

# cpdef int test(int x):
#     cdef int y = 1
#     cdef int i
#     for i in range(1, x+1):
#         y *= i
#     return y


"""Обратите внимание на то, что перед функцией стоит ключевое слово cpdef.
Это позволяет вызывать данную функцию из Python. Кроме того, тип назначен и переменной i,
играющей роль счётчика цикла. Не будем забывать о том, что типизировать нужно все переменные,
объявленные в функции. Это позволит компилятору C узнать о том, какие именно типы ему использовать.
Теперь создадим файл setup.py, который поможет нам преобразовать Cython-код в C-код:"""

# from distutils.core import setup
# from Cython.Build import cythonize
#
# setup(ext_modules = cythonize('run_cython.pyx'))

"""Выполним компиляцию:"""
# python setup.py build_ext --inplace

"""Теперь С-код готов к использованию.

Если взглянуть в папку, в которой находится Cython-код, там можно будет найти все файлы,
необходимые для запуска C-кода, включая файл run_cython.c. Если вам интересно — откройте этот файл и посмотрите на то,
какой С-код сгенерировал Cython.

Теперь всё готово к тестированию нашего сверхбыстрого C-кода.
Ниже приведён код, используемый для тестирования и сравнения двух вариантов программы."""

import run_python
import run_cython
from time import perf_counter

numbers = [10, 100, 1000, 10000, 100000]

for number in numbers:
    start = perf_counter()
    run_python.test(number)
    end =  perf_counter()

    py_time = end - start
    print(f"number: {number}")
    print(f"Python time = {py_time}")

    start = perf_counter()
    run_cython.test(number)
    end =  perf_counter()

    cy_time = end - start
    print(f"Cython time = {cy_time}")

    print(f"Speedup = {py_time / cy_time}\n")


"""Cython это правильный олдскульный вариант для ускорения Python кода. Но я давно всем рекомендую Numba.

Одним декоратором можно добиться такой же скорости, как и у Cython без всяких .pyx модулей и С-подобного языка.
Вот рабочий код для факториала:"""

# import run_python
# import run_cython
#
# from time import perf_counter
# from numba import jit
#
# @jit
# def test(x):
#     y = 1
#     for i in range(1, x+1):
#         y *= i
#     return y
#
# number = 1000
#
# begin = perf_counter()
# run_python.test(number)
# print(f"Time for run_python.test({number}): {perf_counter() - begin}")
#
# begin = perf_counter()
# run_cython.test(number)
# print(f"Time for run_cython.test({number}): {perf_counter() - begin}")
#
# begin = perf_counter()
# test(number)
# print(f"Time for @jit test({number}): {perf_counter() - begin}")