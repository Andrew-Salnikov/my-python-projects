# демонстриурет запись в текстовый файл
print("Создаю текстовый файл методом write()")
file = open("write_it.txt", "w", encoding = 'utf-8')
file.write("Строка 1\n")
file.write("Это строка 2\n")
file.write("Этой строке достался номер 3\n")
file.close()
print("\nЧитаю вновь созданный файл: ")
file = open("write_it.txt", "r", encoding = 'utf-8')
print(file.read())
file.close()
print()
print("Создаю текстовый файл методом writelines()\n")
file = open("write_it.txt", "w", encoding = 'utf-8')
lines = ["Строка 1\n",
         "Это строка 2\n",
         "Этой строке достался номер 3\n"]
file.writelines(lines)
file.close()
print("\nЧитаю вновь созданный файл: ")
file = open("write_it.txt", "r", encoding = 'utf-8')
print(file.read())
file.close()

input("Press Enter to exit")