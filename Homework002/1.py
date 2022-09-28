# Задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

def sum_nums(a):
    sum_ = 0
    for i in str(a):
        if i != ".":
            sum_ += int(i)
    return sum_


a = input('Введите число: ')
print(sum_nums(a))