# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#SWAP THEM!!!

color = input('Enter your favorite colors (through a space): ')
h = color.split(' ')
for k in range(1, len(h), 2):
    h[k], h[k -1] = h[k - 1], h[k]
print(h)
auto = input('Enter your favorite car brands (through a space): ')
m1 = color + ' ' + auto
i = m1.split(' ')
print(i)
for k in range(1, len(i), 2):
    i[k], i[k -1] = i[k - 1], i[k]
print(i)
