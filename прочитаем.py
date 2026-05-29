# демонстриурет чтение из текстового файла
print("Открываю и закрываю файл")
file = open("read_it.txt", "r", encoding = 'utf-8')
file.close()
print("\nЧитаю посимвольно: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
print(file.read(1))
print(file.read(5))
file.close
print("\nЧитаю целиком: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
print(file.read())
file.close()
print("\nЧитаю одну строку посимвольно: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
print(file.readline(1))
print(file.readline(5))
file.close()
print("\nЧитаю одну строку целиком: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
print(file.readline())
print(file.readline())
file.close()
print("\nЧитаю весь файл в список: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
lines = file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
file.close()
print("\nПеребираю файл построчно: ")
file = open("read_it.txt", "r", encoding = 'utf-8')
for line in file:
    print(line)
file.close()

input("\n\nPress Enter to exit")



