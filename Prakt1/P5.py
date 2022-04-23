summa_v = float(input('введите ссумму выручки'))
summa_minus = float(input('введите сумму издержек'))
summa_rent = float(summa_v / summa_minus)

if summa_v < summa_minus:
    print('Вы в минусе, соберитесь')
if summa_v == summa_minus:
    print('Вы вышли в ноль, наймите аналитика')
elif summa_v > summa_minus:
    n_people = int(input('Сколько у Вас соктрудников?'))
    n_people = float(n_people)
    summa_h = summa_rent / n_people
    print(f'Таки Вы в плюсе, так держать! Рентабельность составила {summa_rent:.2f}, прибыь фирмы на одного сотрудника составляет {summa_h:.2f}')