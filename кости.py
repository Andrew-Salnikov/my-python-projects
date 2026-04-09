print('\n\t\t\tПрограмма \'Кости\'')
#Демонстрирует генерацию случайных чисел
import random
#создаем случайные числа из диапазона 1 - 6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
total = die1 + die2
print(f'При вашем броске выпало {die1} и {die2}.'
      f'\nОчков в сумме {total}')
input('\n\n\t\t\tPress Enter to key for exit')
