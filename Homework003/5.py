# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input())

fib1 = 0
fib2 = 1
u1 =[fib1, fib2]
for i in range(2, k +1):
    fib1, fib2 = fib2, fib1 + fib2
    u1.append(fib2)

u2 = []
for i in range(k + 1):
    u2.append(((-1)**(i+1))*u1[i])
u1.remove(0)

print(list(reversed(u2)) + u1)
