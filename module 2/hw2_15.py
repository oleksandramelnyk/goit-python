'''Напишите программу, которая будет выполнять простейшие математические операции с числами последовательно, принимая от пользователя операнды (числа) и оператор.

Условия приёмки

Приложение работает с целыми и дробными числами.
Приложение умеет выполнять такие математические операции:
СЛОЖЕНИЕ (+)
ВЫЧИТАНИЕ (-)
УМНОЖЕНИЕ (*)
ДЕЛЕНИЕ (/)
Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
Все операции приложение выполняет по мере поступления — одну за одной.
Приложение выводит результат вычислений, когда получает от пользователя =.
Приложение заканчивает свою работу после того, как выведет результат вычисления.
Пользователь по очереди вводит числа и операторы.
Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
Приложение корректно обрабатывает ситуацию некорректного ввода (exception).
Начальные переменные:

result = None
operand = None
operator = None
wait_for_number = True
result — сюда помещаем итоговый результат operand — всегда хранит текущее число operator — строковый параметр, 
может содержать четыре значения, "+", "-", "*", "/" wait_for_number — флаг, который указывает, что ожидают на вводе, оператор (operator) или операнд (operand)'''

result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input(">>> ")
    if user_input == "=":
        print(result)
        break
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print("Not a number")
            continue
        wait_for_number = False
        if not result:
            result = operand
        else:
            if operator == "+":
                result += operand
            if operator == "-":
                result = result - operand
            if operator == "*":
                result = result * operand
            try:
                if operator == "/":
                    result = result / operand
            except ZeroDivisionError:
                print('ZeroDivisionError')
    else:
        if user_input in ("+", "-", "*", "/"):
            operator = user_input
        else:
            operator = None
        if not operator:
            print("Not operator")
        else:
            wait_for_number = True
