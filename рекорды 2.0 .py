# рекорды 2.0
# демонстрирует вложенные последовательности
scores = []
choice = None
while choice != '0' :
    print(
    '''
    Рекорды 2.0
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорды
    '''
    )
    choice = input('Ваш выбор: ')
    print()

    if choice == '0':
        print('До свидания!')
    elif choice == '1':
        print('Рекорды\n')
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(f'{name} \t{score}')
    elif choice == '2':
        name = input('Впишите имя игрока: ')
        score = int(input('Введите его результат: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
    else:
        print('Извинте, но нет такого пункта!')

input('Press Enter to exit')
