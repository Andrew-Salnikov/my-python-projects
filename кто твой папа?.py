family = {
    "Владимир Владимирович Путин" : "Владимир Спиридонович Путин",
    "Пушкин Александр Сергеевич" : "Сергей Львович Пушкин",
    "Дональд Трамп" : "Фред Трамп",
    "Гагарин Юрий Алексеевич" : "Алексей Иванович Гагарин",
    "Роберт Оппенгеймер" : "Юлиус Селлегман Оппенгеймер"
}
print("\n\t\t\tБАЗА ДАННЫХ ЗНАЧИМЫХ ЛЮДЕЙ.\n")
menu = (
        '''
        0 - выйти
        1 - найти отца личности
        2 - добавить личность и его отца 
        3 - изменить отца личности
        4 - удалить человека и его отца из базы
        5 - узнать кто дед личности из базы
        '''    
        )
print(menu)
choice = None

while choice != "0":
    choice = input("\nВыберите действие: ")

    if choice == "0":
        print("До свидания!")

    elif choice == "1":  
        person = input("Отца какого человека ты ищешь? ").title()
        if person in family:
            f_person = family[person]
            print(f"Отца {person} звали {f_person}. ")
        else:
            print("Такого человека в нашей базе данных нет. Попробуйте добавить его.")
        print(f"\n{menu}")

    elif choice == "2":
        person = input("Какого человека ты хотел бы добавить в нашу базу данных? ").title()
        if person not in family:
            f_person = input("Как звали отца этого человека? ").title()
            family[person] = f_person
            print(f"Вы успешно добавили {person} и его отца {f_person} в нашу базу данных.")
        else:
            print("Такой человек уже есть базе.")
        print(f"\n{menu}")

    elif choice == "3":
        person = input("Отца какого человека в истории ты хотел бы переписать? ").title()
        if person in family:
            f_person = input("Введите имя его оцта: ").title()
            family[person] = f_person
            print(f"Имя отца {person} успешно изменено на {f_person}")
        else:
            print(f"Такого человека - {person} нет в базе. Попробуйте добавить его. ")
        print(f"\n{menu}")

    elif choice == "4":
        person = input("Какого человека и информацию об его отце ты хотел бы удалить? ").title()
        if person in family:
            del family[person]
            print(f"Информация об {person} успешно удалена. ")
        else:
            print(f"Такого человека - {person} нет в нашей базе данных. ")
        print(f"\n{menu}")

    elif choice == "5":
        def ded():
            answer = input("Введите ФИО личности: ").title()
            if answer == "Владимир Владимирович Путин":
                deda = "Дед Владимира Путина"
                print(f"Дед {deda}")
            elif answer == "Дональд Трамп":
                deda = "Дед Трампа"
                print(f"Дед {deda}")
            else:
                print("Неверный выбор, попробуйте снова")
            print(f"\n{menu}")
        ded()

    else:
        print("Не верный ввод. Попробуйте заново. ")
        print(f"\n{menu}")

input("Press Enter to exit")
