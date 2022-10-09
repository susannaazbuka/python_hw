# 1. Вычислить число π c заданной точностью d
# *Пример:*
# при d = 0.001, π = 3.141. 10^{-1} ≤ d ≤ 10^{-10}


import decimal
def calc_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi

n = list(map(str, input('Введите точность числа π в формате десятичной дроби (например, 0.001): ').split('.')))
d = len(n[1])
print(f'Число π с {d} цифрами после зяпятой равно {calc_pi(d)}.')
