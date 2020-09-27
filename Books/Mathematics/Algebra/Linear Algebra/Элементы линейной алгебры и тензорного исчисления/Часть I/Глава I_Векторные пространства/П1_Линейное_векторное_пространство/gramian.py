"""Линейная независимость функций. Определители Вронского и Грама
http://mathhelpplanet.com/static.php?p=linyeinaya-nezavisimost-funktsii
http://pmpu.ru/vf4/dets/gram
"""

"""Теорема. Для того, чтобы система функций y1(x), y2(x),..., yn(x) была линейно зависимой,
необходимо и достаточно, чтобы ее определитель Грама равнялся нулю."""

from pprint import pprint
from sympy import *

x = symbols('x')
pi = pi

def get_gramian(funcs: list) -> float:
    """Вычисляет грамиан данной системы функций (векторов)."""

    # Матрица Грама
    M = Matrix([])
    # Заполнение матрицы Грама
    for i in range(len(funcs)):
        row = []
        for j in range(len(funcs)):
            row.append(integrate(funcs[i] * funcs[j], (x, -pi, pi)))
        M = M.row_insert(i, Matrix([row]))
    print('M:')
    pprint(M)
    print()
    # Вычисление грамиана (определителя Грама)
    return M.det()


# Задание 15. Доказать линейную зависимость следующих систем функций
# а). 1, sin(x), cos(x), sin(x)**2, cos(x)**2,...,sin(x)**n, cos(x)**n (n >= 2)
funcs = [1, sin(x), cos(x),
         sin(x)**2, cos(x)**2]
gramian = get_gramian(funcs)
print(f"gramian = {gramian}")
print(f"Грамиан равен нулю, следовательно система функций линейно зависима.\n" if not gramian
      else "Грамиан не равен нулю.\n")

# б). sin(x), cos(x), sin(x)**2, cos(x)**2,...,sin(x)**n, cos(x)**n (n >= 4)
funcs = [sin(x), cos(x),
         sin(x)**2, cos(x)**2,
         sin(x)**3, cos(x)**3,
         sin(x)**4, cos(x)**4]
gramian = get_gramian(funcs)
print(f"gramian = {gramian}")
print(f"Грамиан равен нулю, следовательно система функций линейно зависима.\n" if not gramian
      else "Грамиан не равен нулю.\n")
