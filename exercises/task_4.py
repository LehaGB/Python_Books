#Задача № 4
#Покупатель приобретает в магазине пять товаров.
#Напишите программу,  которая запрашивает цену каждого товара и затем выводит
# накопленную стоимость  приобретаемых товаров, сумму налога с продаж и итоговую сумму.
#Допустим, что налог с продаж составляет 7%.

tax = 0.07
product1 = int(input('Введите цену первого товара: '))
product2 = int(input('Введите цену второго товара: '))
product3 = int(input('Введите цену третьего товара: '))
product4 = int(input('Введите цену четвёртого товара: '))
product5 = int(input('Введите цену пятого товара: '))

accumulated_value = product1 + product2 + product3 + product4 + product5
print(f'Сумма приобретенных товаров: {accumulated_value}')

the_amount_of_tax = accumulated_value * tax
print(f'Сумма налога с продаж: {the_amount_of_tax:.2f}')

the_total_amount = accumulated_value - the_amount_of_tax
print(f'Итоговая сумма: {the_total_amount:.2f}')
