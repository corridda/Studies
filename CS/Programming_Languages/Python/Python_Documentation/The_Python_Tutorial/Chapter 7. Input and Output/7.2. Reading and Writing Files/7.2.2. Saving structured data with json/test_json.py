import json

print(json.__all__)
print(json.dumps([1, 'simple', 'list']))

x = [1, 2, 3, 4, 5]
with open('text3.txt', 'w') as f:
    json.dump(x, f)

with open('text3.txt', 'r') as f:
    x_loaded = json.load(f)
    print(f'x_loaded: {x_loaded}')
