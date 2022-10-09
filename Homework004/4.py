# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os


dict_ = {
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}


k = int(input('Введите степень k от 1 до 9: '))   # наибольшая степень из всех многочленов
str_ = f'{random.randrange(11)}*x{dict_[k]} + {random.randrange(11)}*x{dict_[k-1]} + {random.randrange(11)} = 0'
print(str_)

with open(os.path.dirname(os.path.abspath(__file__)) + '/new_file', 'w', encoding='utf-8') as f:
    f.write(str_)

print('Проверьте файл new_file.')
