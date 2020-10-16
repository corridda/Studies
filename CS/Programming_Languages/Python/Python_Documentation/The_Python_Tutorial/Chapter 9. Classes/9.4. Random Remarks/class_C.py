# Function defined outside the class
def f1(self, x, y):
    return min(x, y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c_obj = C()
print('c_obj.f(10, -5):', c_obj.f(10, -5))
print('c_obj.h():', c_obj.h())


class D:
    f = f1

d_obj = D()
print('d_obj.f(-5, -20):', d_obj.f(-5, -20))