# рекорды 2.0
# демонстрирует вложенные последовательности
scores = []
choice = None
print('''
      Рекорды 2.0
      0 - Выйти
      1 - Показать рекорд
      2 - Добавить рекорд
      ''')
while choice != 0:
    choice = int(input('\nВведите ваш выбор: '))
    if choice == 0:
        print('До свидания!')
    elif choice == 1:
        print('ИМЯ\tРЕКОРД')
        for score in scores:
            name, rez = score
            print(f'{name}\t{rez}')
    elif choice == 2:
        name = input('Введите имя рекордсмена: ')
        rez = int(input('Введите его результат: '))
        score = (rez, name)
        scores.append(score)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print('Не верный выбор! ')
input('Press Enter to exit')