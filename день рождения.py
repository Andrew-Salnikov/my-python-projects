# День рождения
# Демонстрирует именованные аргументы и значения параметров по умолчанию

# Позиционные параметры
def birthday1(name,age):
    print(f"С днём рождения, {name}! Вам сегодня исполняется {age}!\n")

# параметры со значениями по умолчанию
def birthday2(name = "Товарищ Иванов", age = 25):
    print(f"С днём рождения, {name}! Вам сегодня исполняется {age}!\n")

birthday1("Товарищ Иванов", 25)
birthday1(1, "Товарищ Иванов")
birthday1(name = "Товарищ Иванов", age = 1)
birthday1(age = 1, name = "Товарищ Иванов")
birthday2()
birthday2(name = "Катя")
birthday2(age = 12)
birthday2(name = "Катя", age = 12)
birthday2("Катя", 12)
input("\n\nPress Enter to exit")