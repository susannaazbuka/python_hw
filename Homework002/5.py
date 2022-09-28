# Задание 5. Реализуйте алгоритм перемешивания списка.

u = list(range(5))
print(f'Первоначальный список: {u}.')

import random
def shuffle_manual(u):
    array_len = len(u)
    for i in range(array_len):
        temp = random.randrange(array_len - 1)
        u[i], u[temp]  = u[temp], u[i]


def shuffle(u):
    copy = list(u)
    shuffle_manual(copy)
    return copy


print(f'Перемешанный список: {shuffle(u)}.')