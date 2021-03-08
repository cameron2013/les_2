# Второе задание
my_list = [0, ]
my_list.insert(0, input("Введите первый элемент: "))
my_list.pop(1)
n = 1
while True:
    q = input("Нужно большое элементов? Да - любое; Нет - 0. ")
    if q == '0':
        break
    my_list.append(input("Введите элемент: "))
    n += 1
print(my_list)
i = 0
if n % 2 == 0:
    while i < n - 1:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
else:
    while i < n - 2:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
print(my_list)
