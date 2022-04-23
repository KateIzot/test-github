n_init = int(input('Введите целое положительное число'))
Max_n = 0
n = n_init

while n > 0:
    digit = n % 10
    if digit > Max_n:
        Max_n = digit
        if Max_n == 9:
            break
    n = n // 10

print(f'Наибольшая чифра в числе {n_init} равна {Max_n}')


