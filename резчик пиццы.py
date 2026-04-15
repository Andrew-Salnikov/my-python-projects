# Резчик пиццы
# Демонстрирует срезы строк 
word = 'Пицца'
print (
'''
 0   1   2   3   4   5
 +---+---+---+---+---+ 
 | п | и | ц | ц | а | 
 +---+---+---+---+---+ 
-5  -4  -3  -2  -1
'''
)
print('Введите начальный и конечный индексы для того среза "пиццы", который хотите получить')
print('Для выхода нажмите Enter, не вводя начальную позицию')
start = None
while start != '':
    start = (input('\nНачальная позиция: '))
    if start:
        start = int(start)
        finish = int(input('Конечная позиция: '))
        print(f'Cрез word [{start}:{finish}] выглядит как', end=' ')
        print(word[start:finish])
    break
input('\n\t\t\tPress Enter to exit')