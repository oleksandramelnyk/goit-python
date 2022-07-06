"""
Напишите функцию real_len, которая подсчитывает и возвращает длину строки без следующих управляющих символов:
[\n, \f, \r, \t, \v]
"""


def real_len(text):
    res = 0

    for i in text:
        if i not in '\n\f\r\t\v':
            res += 1
    return res
