#только согласные
#демонстриурет, как создавать новые строки из исходных с помощью цикла for
message = input('Введите ваше сообщение: ')
UPPER = "уеёэоаыяию"
new_message = ""
for letter in message:
    if letter.lower() not in UPPER:
        new_message += letter
        print(f'Создана новая строка: {new_message}')
print(f'\nВот ваш текст с изъятыми гласными буквами: {new_message}')
