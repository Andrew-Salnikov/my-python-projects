import random
print('Эта программа сгенерирует ваш пароль') 
x = int(input('Введите кол-во символов для вашего пароля: '))
number = '1234567890'
letter = 'qwertyuiopasdfghjklzxcvbnm'
symbol = '±!@#$%^&*()_+'
letter_1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
all = number + letter + symbol + letter_1
password = ''
for i in range(x):
    password += random.choice(all)
print(f'Ваш новый пароль из {x} символов: {password}')