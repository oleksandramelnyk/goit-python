"""
Мы разрабатываем кулинарный блог. И в рецептах, при написании списка ингредиентов,
мы разделяем их запятыми, а перед последним ставим союз "and", как в примере ниже:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов
["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] и возвращать собранную строку из его элементов
в описанный выше способ. Ваша функция должна уметь обрабатывать списки любой длины.
"""


def format_ingredients(items):

    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]

    recipe = ', '.join(items[:-1]) + ' and ' + items[-1]

    print(f"'{recipe}'")
