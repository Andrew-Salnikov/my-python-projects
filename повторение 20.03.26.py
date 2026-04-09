#Программа, которая использует if else elif и ветвления
log = 'admin'
pas = 1234
login = input('Введите логин: ')
password = int(input('Введите пароль: '))
if not login or not password:
    print('Заполните все поля')
else:
    if log != login:
        print('Неверный логин,'
              '\nдоступ запрещен.')
    elif pas != password:
         print('Неверный пароль,'
              '\nдоступ запрещен.')
    else:
        print('Вы успешно авторизованы')
input("\n\n\t\t\tPress enter to key exit\n")

#программа, которая использует проверку на пустоту
money = int(input('Добро пожаловать в наш ресторан. К сожалению, все столики'
                  '\nсейчас заняты...  Подскажите, какую сумму чаевых вы готовы'
                  'заплатить? '))
if money:
    print('Здорово! Мы сейчас же найдем для вас столик')
else:
    print('К сожалению, вам придется подождать свободный столик...')
input('\n\n\t\t\tPress the enter key to exit\n')


#программа, которая использует иннциализацию управляющей переменной
print('Иммитируется разговор с трехлетним ребенком')
print('Попробуйте остановить этот кошмар')
qs = ''
while qs != 'потому что':
    qs = input('почему? ')
input("\n\n\t\t\tPress enter to key exit\n")

#программа, которая использует составные операторы
trolls = 0
health = 10
damage = 3
while health >= 0:
    print(f'Наш бравый воин убивает троля, но получает урон на {damage} очка!')
    trolls += 1
    health -= damage
print(f'Воин побеждает, он убил {trolls} троллей, но сам погиб!')
input('\n\n\t\t\tPress the enter key to exit\n')

