menu = ("""
        0 - Войти в аккаунт
        1 - Создать аккаунт
        2 - Просмотр всех аккаунтов
        3 - Изменить пароль на своём аккаунте
        4 - Удалить свой аккаунт
        5 - Выйти из программы
        """)
import shelve 
def open_file():
    try:
        file = shelve.open("akk_file.dat")
    except IOError as e:
        print(f"Не удалось создать dat-файл по причине: {e}")
    return file


def make_akk():
    login = input("Введите логин: ").lower()
    print("Загружаю информацию в dat-файл...")
    try:
        password = int(input("Введите пароль, состоящий из цифр: "))
        print("Загружаю и шифрую информацию в dat-файл...")
    except ValueError as e:
        print("Неверный формат ввода пароля, попробуйте заново.")
        print(f"Код ошибки - {e}")
    print(f"Информация по аккаунту {login} сохранена.")
    return login, password

try:
    login, password = make_akk()
    print(f"Создаю аккаунт. Логин - {login}")
    if password:
        file = open_file()
        file[login] = [password]
        print("Пароль успешно сохранён.")
        file.close()
except UnboundLocalError as e:
    print("Вы ввели неверный формат пароля. Попробуйте еще раз.")



#Смотри, я тут сделал создание и сохранение инфы (логин + пароль). 
#Тебе нужноо еще раз погрузиться с вариантом че делать, если пароль введется криво
#А так дальше по ТЗ, вроде не сложно будет 
file = open_file()
if file[login]:
    print("ИНфа есть отдыхай заебал")







