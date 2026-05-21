menu =    """\n\n
   💵 ДОБРО ПОЖАЛОВАТЬ 💵
   Выберите действие :
   0 - Выйти
   1 - Создать личный кабинет
   2 - Проверить баланс
   3 - Пополнить счет / сделать перевод
   4 - Изменть личные данные 
   5 - Удалить личный кабинет\n\n
    """
print(menu)

choice = input("\nВыберите один из пунктов меню ⬆️: ")
lk = {}

def creat_lk():
    login = input("Введите свой номер телефона: ")
    password = input("Придумайте пароль для личного кабинета: ").lower()
    lk[login] = {
        "password": password,
        "money": 0
    }
    print(f"\n\nПривязываем номер {login} к серверной части...")
    print("Создаем личный кабинет...")
    print("Готово! Вы можете воспользоваться личным кабинетом, выбрав 2 или 3 пункт меню!✅✅✅")

def check_login():
    login = input("Введите номер телефона: ")
    return login


def check_balance():
    login = check_login()
    if login in lk:
        password = input("Введите пароль: ").lower()
        if lk[login]["password"] == password:
            print("\nВы успешно авторизованы!")
            print(f"Ваш текущий баланс: {lk[login]['money']} рублей!")
        else:
            print("\nНеверный пароль. Попробуйте зайти снова. ")
    else:
        print("Несуществующий логин. Попробуйте создать личный кабинет. ")

def top_up():
    login = check_login()
    if login in lk:
        password = input("Введите пароль: ").lower()
        if lk[login]['password'] == password:
            print("\nВы успешно авторизованы!")
            print(f"Ваш текущий баланс: {lk[login]['money']} рублей!")
            new_money = int(input("\nВведите сумму пополнения: "))
            lk[login]["money"] += new_money
            print("Баланс успешно пополнен. Чтобы проверить воспользуйтесь пунктом 2. ")
        else:
            print("\nНеверный пароль. Попробуйте зайти снова. ")
    else:
        print("Несуществующий логин. Попробуйте создать личный кабинет или повторите вход. ")

def transaction():
    login = check_login()
    if login in lk:
        password = input("Введите пароль: ").lower()
        if lk[login]['password'] == password:
            print("\nВы успешно авторизованы!")
            print(f"Ваш текущий баланс: {lk[login]['money']} рублей!")
            number = input("Введите номер для перевода: ")
            trans = int(input("Введите сумму перевода: "))
            if trans < lk[login]['money']:
                print("Перевод успешно выполнен.")
                lk[login]['money'] -= trans
            else:
                print("Недостаточно средств. Попробуйте поплнить счет")
        else:
            print("\nНеверный пароль. Попробуйте зайти снова. ")
    else:
        print("Несуществующий логин. Попробуйте создать личный кабинет или повторите вход. ")

def change():
    login = check_login()
    if login in lk:
        password = input("Введите старый пароль: ").lower()
        if password == lk[login]['password']:
            new_password = input("Введите новый пароль: ")
            lk[login]['password'] = new_password
            print("Пароль успешно изменен. ") 
        else:
            print("Неверный пароль, попробуйте снова")
    else:
        print("Такого аккаунта не существует")

def dell():
    login = check_login()
    if login in lk:
        del lk[login]
        print(f"Аккаунт по номеру {login} удалён. ")
    else:
        print("Такого аккаунта не существует. ")
    
while choice != "0":
    if choice == "1":
        creat_lk()
        print(menu)
        choice = input("Выберите действие : ")
    elif choice == "2":
        check_balance()
        print(menu)
        choice = input("Выберите действие : ")
    elif choice == "3":
        answer = input("Вы хотите пополнить счет или сделать перевод? ").lower()
        if answer == "пополнить":
            top_up()
        elif answer in ["сделать перевод", "перевод"]:
            transaction()
        else:
            print("Неверный вариант ответа. Попробуйте заново.")
        print(menu)
        choice = input("Выберите действие : ")
    elif choice == "4":
        change()
        print(menu)
        choice = input("Выберите действие : ")
    elif choice == "5":
        dell()
        print(menu)
        choice = input("Выберите действие : ")
    else:
        print("Такого пункта выбора не существует. ")
        print(menu)
        choice = input("Выберите действие : ")

input("press enter to exit")
