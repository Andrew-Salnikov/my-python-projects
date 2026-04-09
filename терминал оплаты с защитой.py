print('\n\n\t\t\tTЕРМИНАЛ ОПЛАТЫ')
summ = int(input('\nВведите сумму к оплате(мы проверим) :'))
import random
pay = random.randint(1,1000)
print(f'Получили ваши деньги в размере {pay} рублей')
if summ == pay:
    print('Вот это совпадение реально... Заберите товар')
elif summ > pay:
    raz = summ - pay
    print(f'Извините, но вам не хватает {raz} рублей для получения товара ')
elif summ < pay:
    sdc = pay - summ
    print(f'Покупка совершена, заберите товар и сдачу {sdc} рублей')
input('\n\n\t\t\tPress Enter to key for the exit')
