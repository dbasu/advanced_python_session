x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]

print(x[2]['bar']['z'])


print('m' in x[2]['bar'])



print(x[2]['bar'].get('w', -1))

x[2]['bar'].setdefault('w', 0) 
print(x[2]['bar'].get('w', -1))

x = {'foo':1, 'bar':2, 'baz':3}
y = dict(qux=4, quux=5, quuz=6, bar=7)


z1 = {**x, **y}

z2 = x.copy()
z2.update(y)
z3 = {**y, **x}
print(z1)
print(z2)
print(z3)
