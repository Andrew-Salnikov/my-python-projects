print('Программа "Калькулятор". Он работает.'
      '\nТакже данная программа запоминает 5 последних ваших вычислений.')
print(
    '''
    Выберите действие:
    0 - выйти
    1 - сложение
    2 - вычитание
    3 - деление
    4 - умножение
    5 - показать 5 последних вычислений
    ''')
choice = None
operations = []

while choice != 0:
    print()
    choice = int(input('Введите номер операции: '))
    if choice == 0:
        print('До свидания!')
    
    elif choice == 1:
        x = int(input('Введите первое слогаемое: '))
        y = int(input('Введите второе слогаемоемое: '))
        rez = x + y 
        print(f'Сумма ваших чисел равна {rez}')
        operations.append(rez)
        operations = operations[:5]
        continue
    
    elif choice == 2:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        rez = x - y 
        print(f'Разность ваших чисел равна {rez}')
        operations.append(rez)
        operations = operations[:5]
        continue

    elif choice == 3:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        if y != 0:
            rez = x/y 
            operations.append(rez)
            operations = operations[:5]
            print(f'Полученное число {rez}')
            continue
        else: 
            print('На ноль делить нельзя!')
            continue
    
    elif choice == 4:
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        rez = x * y 
        print(f'Полученное число {rez}')
        operations.append(rez)
        operations = operations[:5]
        continue

    elif choice == 5:
        print(operations)
        continue

    else: 
        print('Не верный ввод для вычислений. ')
        continue

input('Press Enter to exit')