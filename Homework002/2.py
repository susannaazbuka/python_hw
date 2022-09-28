# Задание 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.


def factorial_(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f


def fill_list(n):
    u = []
    for i in range(1, n + 1):
        u.append(factorial_(i))
    return u


print(fill_list(int(input("Введите N: "))))

