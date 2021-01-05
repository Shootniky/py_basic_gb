# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# for the list
month = int(input('Enter number from 1 - 12: '))
ls = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Semptember', 'October', 'November']
winter = ls[0:3]
spring = ls[3:6]
summer = ls[6:9]
autumn = ls[9:12]
if month ==  3 or month < 6:
    print('Your month is spring', spring)
elif month == 6 or month < 9:
    print('Your month is summer', summer)
elif month == 9 or month < 12:
    print('Your month is autumn', autumn)
else:
    print('Your month is winter', winter)


