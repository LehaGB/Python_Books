#Множества.
s = {'Moscov', 'Piter', 34,}
for x in s:
    print(f'{x}')
print(type(s))

#Словарь.
a = int(input('Введите ключ, чтоб найти значение: '))
d = {'Moscov': 123, 'Piter': 456, 'Rostov': 789}
for el in d:
    if d[el] == a:
        print(f'{el}')


print(type(d))