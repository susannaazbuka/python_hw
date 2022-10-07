# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

#u = [float(number) for number in input().split(', ')]
u = [1.1, 1.2, 3.1, 5, 10.01]                       # работает только с положительными вещ.числами
max_fraction = (u[0]%1)
min_fraction = (u[0]%1)

for i in range(len(u)):
    print(u[i], '>>', float(round((u[i]%1), 2)))
    if round(u[i]%1, 2) == 0:
        continue
    if round(u[i]%1, 2) > max_fraction:
        max_fraction = round(u[i]%1, 2)
    if round(u[i]%1, 2) < min_fraction:
        min_fraction = round(u[i]%1, 2)

print(round((max_fraction - min_fraction), 2))

