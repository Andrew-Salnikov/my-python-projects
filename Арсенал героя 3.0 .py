# Арасенал героя 3.0
inventory = ['меч', 'кольчуга', 'щит', 'целебное снадобье']
print('\nИтак, в вашем арсенале:')
for item in inventory:
    print(item)

input('\nPress Enter to continue')
print(f'Сейчас в вашем распоряжении {len(inventory)} предмета/-ов.')
input('\n\nPress Enter to continue')

if 'целебное снадобье' in inventory:
    print('Вы еще поживете и повоююте')

index = int(input('\nВведите индекс одного из предметов арсенала: '))
print(f'Под индексом {index} находится {inventory[index]}')

start = int(input('\nВведите начальный индекс среза: '))
finish = int(input('Введите конечный индекс среза: '))
print(f'Срез inventory [ {start} : {finish} ] - это {inventory[start:finish]} ')
input('\n\nPress Enter to continue')


# теперь соеденим два списка
chest = ['золото', 'драгоценные камни']
print('Вы нашли ларец. Вот что в нем есть: ')
print(chest)
print('Вы приобщили содержимое ларца к своему арсеналу')
inventory += chest
print('Теперь в вашем распоряжении: ')
print(inventory)
input('\n\nPress Enter to continue')

# присваиваем значение элементу по индексу
print('Вы обменяли меч на арбалет')
inventory[0] = 'арбалет'
print(f'Теперь ваш арсенал содержит следующие предметы :')
print(inventory)
input('\n\nPress Enter to continue')

# приписываем значение элементам по срезу индексов
print('За золото и драгоценные камни вы купили магический кристалл')
inventory [4:6] = ['магический кристалл']
print('Теперь в вашем распоряжении: ')
print(inventory)
input('\n\nPress Enter to continue')

# удаляем элемент
print('В это тяжелом бою был раздроблен ваш щит')
del inventory[2]
print('Вот что осталось в арсенале')
print(inventory)
input('\n\nPress Enter to continue')

# из списка можно удалить и срез элементов
print('Воры лишили вас арбалета и кольчуги')
del inventory[:2]
print('В арсенале теперь только :')
print(inventory)
input('\n\nPress Enter to exit')


