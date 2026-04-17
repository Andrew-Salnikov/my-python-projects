print('Давайте посчитаем по вашим границам и интервалам!')
start = int(input('Введите начальное число: '))
finish = int(input('Введите конечное число: '))
x = int(input('Введите интервал между числами: '))
for i in range(start, finish+1, x):
    print(i, end = ' ')
