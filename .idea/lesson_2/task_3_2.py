# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#for the dictionary
month = int(input('Enter number from 1 - 12: '))
year = {'winter' : [1, 2, 12], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8], 'autumn' : [9, 10, 11]}
i = month
for k, v in year.items():
    if i in v:
        print(f'Your month is - ',k)


