"""
Задача № 9: Преобразователь температуры по шкале Цельсия в температуру по шкале Фаренгейта.
Напишите программу, которая преобразует показания температуры по шкале
Цельсия в температуру по шкале Фаренгейта на основе формулы: F = (9/5) * C + 32
Программа должна попросить пользователя ввести температуру по шкале Цельсия и
показать температуру , преобразованную по шкале Фаренгейта.
"""
temperature = int(input('Введите температуру: '))
fahrenheit = (9 / 5) * temperature + 32

print(f'Температура по Фаренгейту {fahrenheit:.0f} градусов')