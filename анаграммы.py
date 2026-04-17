# Анаграммы
# Компьютер выбирает какое либо слово и хаотически переставляет его буквы
# задача игрока - восстановить исходное слово
import random
WORDS = ('питон','игра','весело')
word = random.choice(WORDS)
correct = word
# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ''
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
# начало игры
print(
'''
        Добро пожаловать в игру!
    Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводят своей версии.) 
'''
)
print(f'Вот анаграмма - {jumble}.')
guess = input('Введите предполагаемое слово: ')
attemps = 1
while guess != correct and guess != '':
    print('Это не верный ответ, попробуйте снова!')
    help = input('Тебе нужна подсказка? ')
    if help.lower() == 'да':    
        if correct == 'питон':
            print('Название нашего языка на сленге (подсказываю)')
        elif correct == 'игра':
                print('Типичная детская забава (подсказываю)')
        else:
            print('Ощущение человека, когда ему радостно и интересно (подсказываю)')
    guess = input('Введите предполагаемое слово: ')
    attemps += 1 
    if guess == correct:
        break

print(f'Поздравляю, вы угадали с {attemps} попытки!')

if attemps < 2:
    print('Вы набрали 10 из 10 баллов!')
if 2 <= attemps < 5:
    print('Вы набрали 5 из 10 баллов!')
if 5 < attemps < 100:
    print('Вы набрали 1 балл!')

print('Спасибо за игру.') 
input('\n\t\t\tPress Enter to exit')