with open('d:\\newfile.txt', 'w', encoding='utf-8') as g:
    d = int(input())
    print(f'1 / {d} = {1/d}', file=g)