# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

u = [2, 3, 4, 5, 6]

if  len(u)%2 == 0:
    halfsize = round(len(u)/2)
else:
    halfsize = round(len(u)/2) + 1

product_of_numb = []
for i in range(halfsize): 
    product_of_numb.append(u[i] * u[len(u)-1 -i]) 
print(product_of_numb)