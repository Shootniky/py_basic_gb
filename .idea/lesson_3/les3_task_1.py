# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def del_func ():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    try:
        res = first_number / second_number
        return res
    except ZeroDivisionError:
        print("Error! ZERO!")
calc_del = del_func()
print(f"Two positions arguments divide first / second  =  {calc_del}")

















