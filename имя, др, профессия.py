def get_person_info():
    """Возвращаем кортеж с информацией о деде"""
    database = {
        "Владимир Путин": ("Спиридон Путин", 1879, "повар"),
        "Иосиф Сталин": ("Виссарион Джугашвили", 1850, "ресторатор")
    }
    person = input("Введите имя: ").tittle()
    grandpa, year, job = get_person_info(person)
    choice = None
    while choice != 0:
        print(
        '''
        1 - показать информацию
        0 - выйти
        '''
        )
        if choice == 1:
            if grandpa:
                print(f"Дед {person}: ")
                print(f"Имя: {grandpa}")
                print(f"Год рождения: {year}")
                print(f"Профессия: {job}")
            else:
                print("Информация не найдена")
        elif choice == 0:
            print("До свидания! ")
        else:
            print("Неверный ввод.")
get_person_info()
input("Press Enter to exit")
        
        