SKILLS = ["мощный удар", "сокрушитель брони", "регенерация", "живучесть","уклонение","двойной удар","медитация","проклятие"]
print("У вас на выбор есть 8 скиллов:\n")
for i in range(len(SKILLS)):
    print(SKILLS[i])
print("\nЛюбой из них вы можете добавить к предложенной характеристике: ")
print("СИЛА")
print("ЗДОРОВЬЕ")
print("МУДРОСТЬ")
print("ЛОВКОСТЬ")
print()
menu = (
    '''
     Меню действий:
     0 - выйти
     1 - добавить скилл к характеристике
     2 - вернуть скилл в общий пул
     3 - показать текущий общий пул
     4 - показать текущие скиллы СИЛЫ
     5 - показать текущие скиллы ЗДОРОВЬЯ
     6 - показать текущие скиллы МУДРОСТИ
     7 - показать текущие скиллы ЛОВКОСТИ
    '''
    )
print(menu)
choice = None
sila = []
health = []
mydrost = []
lovkost = []
while choice != 0:
    choice = int(input("\nВыберите действие: "))
    if choice == 0:
        print("До свидания!")

    elif choice == 1:
        skill = input("Какой из этих скиллов вы хотели бы выбрать? ").lower()
        if skill in SKILLS:
            SKILLS.remove(skill)
            har = input(f"К какой характеристике вы хотите добавить скилл {skill}: ")
            if har.upper() == "СИЛА":
                sila.append(skill)
                print(f"Скилл {skill} успешно добавлен к характеристике {har}")
            elif har.upper() == "ЗДОРОВЬЕ":
                health.append(skill)
                print(f"Скилл {skill} успешно добавлен к характеристике {har}")
            elif har.upper() == "МУДРОСТЬ":
                mydrost.append(skill)
                print(f"Скилл {skill} успешно добавлен к характеристике {har}")
            elif har.upper() == "ЛОВКОСТЬ":
                lovkost.append(skill)
                print(f"Скилл {skill} успешно добавлен к характеристике {har}")
            else:
                print(f"Мы не нашли характеристики {har}")
        else:
            print(f"Такого скилла {skill} не было в предложенных")

    elif choice == 2:
        skill = input("Какой скилл вы хотели бы вернуть в общий пул? ").lower()
        SKILLS.append(skill)
        if skill in sila:
            sila.remove(skill)
            print(f"Скилл {skill} успешно возвращен в общий пул. ")
        elif skill in health:
            health.remove(skill)
            print(f"Скилл {skill} успешно возвращен в общий пул. ")
        elif skill in mydrost:
            mydrost.remove(skill)
            print(f"Скилл {skill} успешно возвращен в общий пул. ")
        elif skill in lovkost:
            lovkost.remove(skill)
            print(f"Скилл {skill} успешно возвращен в общий пул. ")
        else:
            print(f"Мы не нашли такого скилла - {skill} ни в одной из характеристик.")

    elif choice == 3:
        print("ОБЩИЙ ПУЛ ВЫГЛЯДИТ СЕЙЧАС ТАК:\n ")
        for i in range(len(SKILLS)):
            print(SKILLS[i])
    elif choice == 4:
        print("СИЛА ВЫГЛЯДИТ СЕЙЧАС ТАК:\n ")
        for i in range(len(sila)):
            print(sila[i])
    elif choice == 5:
        print("ЗДОРОВЬЕ ВЫГЛЯДИТ СЕЙЧАС ТАК:\n ")
        for i in range(len(health)):
            print(health[i])
    elif choice == 6:
        print("МУДРОСТЬ ВЫГЛЯДИТ СЕЙЧАС ТАК:\n ")
        for i in range(len(mydrost)):
            print(mydrost[i])
    elif choice == 7:
        print("ЛОВКОСТЬ ВЫГЛЯДИТ СЕЙЧАС ТАК:\n ")
        for i in range(len(lovkost)):
            print(lovkost[i])

    else:
        print("В меню выбора нет такого варианта! ")

input("Press Enter to exit")

            
            

    

