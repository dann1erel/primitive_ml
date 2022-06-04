import random


# Задание 1. Датчик случайных чисел
# 0 - 1-я (красная) строка/столбец
# 1 - 2-я (синяя)  строка/столбец
def generator(p):
    if random.random() >= p:
        return 1
    else:
        return 0
