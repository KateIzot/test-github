import nacl


n = input('Введите целое положительное число')
nInt = int(n)
while nInt<0:
    print ('число должно быть положительным (>0)')
    n = input('Введите целое положительное число')
    nInt = int(n)

summa = int(n) + int(n + n) + int(n + n + n)

print(f'{n} + {n+n} + {n+n+n}') 
print(summa)

