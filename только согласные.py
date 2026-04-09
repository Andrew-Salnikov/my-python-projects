#только согласные
#демонстриурет, как создавать новые строки из исходных с помощью цикла for
message = input('Введите текст: ')
new_message = ''
VOWELS = 'уеаоэёяию'
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print(f'Создана новая строка: {new_message}')
print(f'Вот ваш текст с изъятыми гласными буквами: {new_message}')
input('\n\t\t\tPress Enter to exit')
