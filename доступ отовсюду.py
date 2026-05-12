# Десонстрирует работу с глобальными переменными
def read_global():
    print(f"В области видимости функции read_global() значение value равно {value}")
def shadow_global():
    value = -10
    print(f"В области видимости функции shadow_global() значение value равно {value}")
def change_global():
    global value 
    value = -10
    print(f"В области видимости функции change_global() значение value равно {value}")

# основная часть
# value - глобальная перменная потому что сейчас мы находимся в глобальной области вдидимости
value = 10
print(f"В глобальной области видимости значение перменной value стало равным {value}. ")
read_global()
print(f"Вернемся в глобальную область и здесь она по прежнему {value}")
shadow_global()
print(f"Вернемся в глобальную область и здесь она по прежнему {value}")
change_global()
print(f"Вернемся в глобальную область и здесь value изменилась на  {value}")

input("\nPress Enter to exit")