print('Загадай число от 1 до 10, я попробую отгадать его за минимальное кол-во попыток.\n')
attempts = 0
ans = ''
while True:
    ans = input('Это число больше или равно 5? (да/нет) ')
    attempts += 1
    if ans == 'да':
        ans = input('Это число 5? ')
        attempts += 1
        if ans == 'да':
            print('Бинго! Я угадал! ')
            break
        elif ans == 'нет':
            ans = input('Это число больше или равно 8? ')
            attempts += 1
            if ans == 'да':
                ans = input('Это число 8? ')
                attempts += 1
                if ans == 'да':
                    print('Бинго! Я угадал!')
                    break
                elif ans == 'нет':
                    ans = input('Это число 9? ')
                    attempts += 1
                    if ans == 'да':
                        print('Бинго! Я угадал!')
                        break
                    else:
                        print('Получается твоё число 10...')
                        attempts += 1
                        break
            elif ans == 'нет':
                ans = input('Это число 6? ')
                attempts += 1
                if ans == 'да':
                    print('Бинго! Я угадал!')
                    break
                else:
                    print('Значит твоё число 7...')
                    attempts += 1
                    break
    elif ans == 'нет':
        ans = input('Это число больше или равно 3? ')
        attempts += 1
        if ans == 'да':
            ans = input('Это число 3? ')
            attempts += 1
            if ans == 'да':
                print('Бинго!Я угадал!')
                break
            elif ans == 'нет':
                print('Значит твоё число 4...')
                attempts += 1
                break
        elif ans == 'нет':
            ans = input('Это число 1? ')
            attempts += 1
            if ans == 'да':
                print('Бинго! Я угадал!')
                break
            else:
                print('Значит твоё число 2...')
                attempts += 1
                break

print(f'Вот так то! Мне понадобилось всего {attempts} попыток!')
input('\n\n\t\t\tPress Enter to exit')

            
        
