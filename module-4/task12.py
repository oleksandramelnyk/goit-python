"""
Задача: случайный надежный пароль

И наконец третий, последний этап. Используя решения из предыдущих двух задач, напишите функцию get_password,
которая сгенерирует нам случайный надежный пароль и вернет его. Алгоритм простой — мы генерируем пароль с
помощью функции get_random_password и, если он проходит надежность проверкой функцией is_valid_password,
возвращаем его, если нет — повторяем итерацию снова.

Примечание: Хорошей практикой будет ограничить количество попыток (например до 100),
чтобы не получить бесконечный цикл.
"""


from random import randint


def get_random_password():
    result = ""
    count = 0

    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():

    for _ in range(100):
        password = get_random_password()
        if is_valid_password(password):
            return password
    return None
