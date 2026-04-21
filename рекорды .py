# Рекорды
# Днмонстрирует списочные методы
scores = []
choice = None
while choice != '0':
    print(
    '''

    Рекорды
    0 - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    4 - Сортировать список
    '''
    )

    choice = input('Ваш выбор: ')
    print()

    # выход
    if choice == '0':
        print('До свидания')
    # вывод рекордов на экран
    elif choice == '1':
        print('Рекорды')
        for score in scores:
            print(score)
    # добавление рекордов
    elif choice == '2':
        score = int(input('Впишите свой рекорд: '))
        scores.append(score)
    # удаление рекорда
    elif choice == '3':
        score = int(input('Какой из рекордов вы хотели бы удалить? '))
        if score in scores:
            scores.remove(score)
        else:
            print(f'Результат {score} не содержится в списке рекордов!')
    # сортировка рекордов
    elif choice == '4':
        scores.sort(reverse=True)
    # непонятный пользовательский ввод
    else:
        print(f'Извините, в меню нет пункта {choice}')

input('Press Enter to exit')
