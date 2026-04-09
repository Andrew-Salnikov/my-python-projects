print('Программа "Угадай число"'
      '\nТвоя задача угадать число от 1 до 10 за минимальное кол-во попыток!')
name = input('Тебя как звать то хоть ? ')
print(f'Ну удачи тогда, {name}!')
y = 0
import random
x = random.randint(1,10)
user_input = ""
attempts = 0
while True:
    user_input = input('Введите предполагаемое число: ')
    attempts += 1
    if not user_input:
        print(f'{name}, вы ничего не ввели, попробуем снова!')
        continue
    y = int(user_input)
    if y > x:
        print('Это число больше, чем мы загадали.')
    elif y < x:
        print('Это число меньше, чем мы загадали.')
    else:
        print('Бинго! Ты угадал(а)')
        break
print(f'Ты угадал с {attempts} раза!')
input(f'{name}, нажми Enter, чтобы программа закрылась.')

    
