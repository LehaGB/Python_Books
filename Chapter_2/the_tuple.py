#Кортежи.
t = 14, 24, 3, 4, 5, 6
a, b, *rest = t
print(f'{a}, {b}')
print(f'{rest}')

A = [(12, 20),(2, 54), (31, 98)]
for T in A:
    first, last = T
    print(f'First = {first}, Last = {last}')

for i, x in enumerate(A):
    first, last = x
    print(f'{i} = {first}, {last}')

