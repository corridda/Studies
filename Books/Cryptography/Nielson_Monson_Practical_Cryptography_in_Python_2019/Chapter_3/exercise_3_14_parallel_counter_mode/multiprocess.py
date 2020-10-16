from multiprocessing import Pool

def f(x, y):
    return x * y


if __name__ == '__main__':
    with Pool() as p:
        print(p.starmap_async(f, [(2, 3), (4, 5), (6, 7)]).get())


