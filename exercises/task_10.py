"""
Задача № 10
Регулятор ингредиентов. Рецепт булочек предусматривает ингредиенты:
1.5 стакана сахара;
1 стакан масла;
2.75 стакана муки.
С таким количеством ингредиентов этот рецепт позволяет приготовить 48 булочек.
Напишите программу, которая запрашивает у пользователя, сколько булочек он хочет
приготовить, и затем показывает число стаканов каждого ингредиента, необходимого
для заданного количества булочек.
"""
sugar = 1.5
oil = 1
flour = 2.75
number_ingredients = 48
number_buns = int(input("Сколько вы хотите испечь булочек: "))

number_sugar = (sugar / number_ingredients) * number_buns
print(f'Вам на {number_buns} булочек потребуется {number_sugar:.2f} стакана сахара')

number_oil = (oil / number_ingredients) * number_buns
print(f'Вам на {number_buns} булочек потребуется {number_oil:.2f} стакана масла')

number_flour = (flour / number_ingredients) * number_buns
print(f'Вам на {number_buns} булочек потребуется {number_flour:.2f} стакана муки')
