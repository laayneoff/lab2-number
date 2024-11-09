import random

a = random.randint(1,10)
attempt = 3
while attempt>0:
    usernum = int(input('Введите число от 1 до 10: '))
    if usernum == a:
        print ('Вы угадали')
        break
    else:
        print('Вы не угадали')
        attempt -=1