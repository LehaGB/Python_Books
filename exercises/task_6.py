#Задача № 6
#. Напишите программу, которая попросит пользователя ввести величину покупки.
#Затем программа должна вычислить федеральный и региональный налоги с продаж.
#Допустим, что федеральный налог с продаж составляет 5%, а региональный 2.5%.
#Программа должна показать сумму покупки, федеральный налог с продаж,
#региональный налог с продаж, общий налог с продаж и общую сумму продажи.
# (т. е. сумму покупки и общего налога с продаж).

federal_tax = 0.05
regional_tax = 0.025
purchase_amount = float(input('Введите велечину покупки: '))
print(f'Сумма покупки составляет: {purchase_amount}')

amount_federal_tax = purchase_amount * federal_tax
print(f'Федеральный налог с продаж сотавляет: {amount_federal_tax:.2f}')

amount_regional_tax = purchase_amount * regional_tax
print(f'Региональный налог с продаж составляет: {amount_regional_tax:.2f}')

common_tax = amount_federal_tax + amount_regional_tax
print(f'Общий налог с продажи составляет: {common_tax:.2f}')

common_sale = purchase_amount + common_tax
print(f'Общая сумма с продажи вместе с налогами составляет: {common_sale:.2f}')

