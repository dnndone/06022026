N = 15  # 11 в пятеричной

# Функция перевода в пятеричное


def to_f(num):
    n = num
    if n == 0:
        return '0'

    result = ''
    while n > 0:
        # остаток от деления на 5 — очередная цифра
        result = str(n % 5) + result
        # уменьшаем число
        n //= 5

    return result


def from_f(num):
    s = num
    result = 0
    for digit in s:
        # сдвигаем текущее значение на разряд влево
        result = result * 5 + int(digit)

    return result


R_MAX = 0

for N in range(0, 16):
    print(N)
    n_5 = str(to_f(N))
    if N % 2 == 0:
        n_5 = "3"+n_5+str(N % 5)
    else:
        n_5 = str(N % 4)+n_5+"4"
    if from_f(n_5) > R_MAX:
        R_MAX = from_f(n_5)
print(R_MAX)
