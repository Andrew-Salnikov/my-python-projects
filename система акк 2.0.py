
def choice_men():
    
    menu = ("""
        1 - Создать аккаунт
        2 - Просмотр всех аккаунтов
        3 - Изменить пароль на своём аккаунте
        4 - Удалить свой аккаунт
        5 - Выйти из программы
        """)
    print(menu)
    choice = input("\nВыберите нужный пункт меню: ")
    return choice 


def open_file(name, mode):
    try:
        file = open(name, mode , encoding = 'utf-8')
        return file
    except FileNotFoundError as e:
        print("Не удалось открыть файл.")
        print(f"Код ошибки: {e}")

def creat_akk():
    login = input("Придумайте логин: ").lower()
    password = input("Придумайте пароль: ")
    print(f"\nАккаунт {login} успешно создан!")
    return login, password
   

def main():

    choice = choice_men()
    while choice != "5":

        if choice == "1":
            file = open_file("system_akk.txt", "a")
            login, password = creat_akk()
            file.write(f"{login}:{password}\n")
            file.close()
            choice = choice_men()
            
            

        if choice == "2":
            file = open_file("system_akk.txt", "r")
            print("Вот список пользователей: \n")
            lines = file.readlines()
            file.close()
            for line in lines:
                line = line.strip()
                login_from_file, password_from_file = line.split(":")
                print(login_from_file)
            choice = choice_men()

        if choice == "3":
            file = open_file("system_akk.txt", "r")
            login = input("Введите логин аккаунта: ").lower()

            lines = file.readlines()
            file.close()

            new_lines = []
            found = False

            for line in lines:
                line = line.strip()
                login_from_file, password_from_file = line.split(":")

                if login == login_from_file:
                    found = True
                    print(f"Пользователь {login} найден.")
                    password = input("Введите текущий пароль: ")

                    if password == password_from_file:
                        print("Пароль введен верно.")
                        new_password = input("Введите новый пароль: ")
                        new_lines.append(f"{login_from_file}:{new_password}\n")
                        print("Данные сохранены.")
                    else:
                        print("Неверный пароль.")
                        new_lines.append(f"{login_from_file}:{password_from_file}\n")

                else:
                    new_lines.append(f"{login_from_file}:{password_from_file}\n")
            
            if not found:
                print("Аккаунт не найден.")
            
            file = open_file("system_akk.txt", "w")
            for line in new_lines:
                file.write(line)

            file.close()
            choice = choice_men()

        if choice == "4":
            file = open_file("system_akk.txt", "r")
            lines = file.readlines()
            file.close()

            login = input("Введите логин аккаунта, который хотите удалить: ").lower()
            new_lines = []
            found = False

            for line in lines:
                line = line.strip()
                login_from_file, password_from_file = line.split(":")

                if login == login_from_file:
                    found = True
                    print(f"Аккаунт {login} найден.")
                    password = input("Введите пароль от аккаунта: ")

                    if password == password_from_file:
                        print("Пароль введен верно.")
                        print("Аккаунт успешно удалён.")

                    else:
                        print("Неверный пароль.")
                        new_lines.append(f"{login_from_file}:{password_from_file}\n")

                else:
                    new_lines.append(f"{login_from_file}:{password_from_file}\n")

            if not found:
                print("Аккаунт не найден.")
            file = open_file("system_akk.txt", "w")
            for line in new_lines:
                file.write(line)

            file.close()
            choice = choice_men()

main()

input("\n\nPress Enter to exit")






    
        








