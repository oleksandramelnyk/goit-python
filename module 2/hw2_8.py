'''Строка — это итерируемый объект, а, значит, мы можем использовать ее в цикле for. 
Подсчитайте в заданной строке message количество вхождений символа из переменной search. Результат поместите в переменную result.'''

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0

for ch in message:
    if ch == search:
        result += 1
