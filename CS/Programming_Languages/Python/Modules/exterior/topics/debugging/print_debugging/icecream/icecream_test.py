from icecream import ic

def foo(num):
    return num + 5

def hello(user:bool):
    if user:
        ic()
    else:
        ic()

if __name__ == '__main__':
    ic(foo(10))
    ic.configureOutput(includeContext=True)
    ic(foo(10))

    ic.configureOutput(includeContext=False)
    num_1 = 30
    ic(num_1)
    hello(user=True)
