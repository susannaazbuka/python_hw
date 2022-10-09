# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. 
# Степени многочленов могут отличаться.

import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/polynomial1', 'r') as f:
    pol1 = f.read().replace(' ', '')
    print(f'Первый многочлен: {pol1}')
with open(os.path.dirname(os.path.abspath(__file__)) + '/polynomial2', 'r') as f:
    pol2 = f.read().replace(' ', '')
    print(f'Второй многочлен: {pol2}')
a1 = pol1.split('*x^2')
a2 = pol2.split('*x^2')

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if is_number(a1[0]):
    a1[0] = int(a1[0])
else:
    a1.insert(0, 0)

if is_number(a2[0]):
    a2[0] = int(a2[0])
else:
    a2.insert(0, 0)
a3 = a1[0] + a2[0]

print(f'a3: {a3}')
b1 = a1[1].split('*x')
b1[0] = list(b1[0])
b2 = a2[1].split('*x')
b2[0] = list(b2[0])

#b3 = list(b1[0]+b2[0])
if b1[0][0]=='+':
    b3 = int(b1[0][1])
else:
    b3 = -int(b1[0][1])

if b2[0][0]=='+':
    b3 += int(b2[0][1])
else:
    b3 += -int(b2[0][1])
print(f'b3: {b3}')

c3 = int(pol1[(pol1.find('=0'))-1]) + int(pol2[(pol2.find('=0'))-1])
print(f'c3: {c3}')

str_ = f'{a3}x^2+{b3}x+{c3}=0'
print(f'Cумма многочленов: {str_}')


with open(os.path.dirname(os.path.abspath(__file__)) + '/sum_pol', 'w', encoding='utf-8') as f:
    f.write(str_)

print('Проверьте файл sum_pol.')