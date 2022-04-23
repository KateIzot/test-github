second = int(input('Введите количество времени (в секундах): '))
hour = second // 3600 
second %= 3600
minute = second // 60
second %= 60
second = second % (24 * 3600)
print(f'У Вас осталось: {hour} часов, {minute} минут, {second} секунд')