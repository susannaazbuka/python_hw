# 1. Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции


u = [2, 3, 5, 9, 3]
sum_ = 0
for i in range(len(u)):
    if i % 2 != 0:
        sum_ = sum_ + u[i]
        print(u[i])
print(sum_)
    