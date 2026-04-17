# игра отгадай слово по 4 главе 
# ПК загадает рандомное слово из кортежа, а пользователь будет его угадывать 
# ПК сообщит игроку сколько букв в загаданном слове 
# ПК также дает 5 попыток узнать есть ли какая-то буква в слове 
import random
WORDS = ('телефон','машина','любовь')
word = random.choice(WORDS)
print('Игра "Отгадай слово!" ')
print (f'В загаданном слове {len(word)} букв! ')
attempts = 0
answer = ''
trys = len(word)
for letter in word:
    answer = input(f'У тебя есть {trys} попыток отгадать букву в слове. Твои предположения?  ')
    trys += -1
    if answer in word:
        print(f'Да, буква {answer} есть в загаданном слове!')
    else:
        print('Такой буквы нет')

jumble = ''
while jumble.lower() != word:
    jumble = input('Итак, у тебя уже есть предположение? Введи своё слово: ')
    attempts += 1
    if jumble.lower() != word:    
        print('Нет,это не верное слово!')

print(f'Поздравляю! Ты угадал! Загаданное слово {word}.'
      f'\nТебе понадобилось {attempts} попыток!')
input('\n\t\tPress Enter to exit')    