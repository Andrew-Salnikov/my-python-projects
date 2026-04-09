#программа проверки логина и пароля. закрепляет понимание if else elif
#и проверку на пустоту

log = 'admin'
pas = 1234

login = input('Введите логин: ')
password = int(input('Введите пароль: '))

if not login or not password:
    print('Заполните все поля')

else:
    if log != login or pas!= password:
        print('Неверный логин или пароль')
    else:
        print('Вы успешно авторизованы')
input('\n\n\t\t\tPress Etner to key the exit')


