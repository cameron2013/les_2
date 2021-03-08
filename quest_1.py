# Первое задание
# Автоматический ввод правильный
my_list_1 = [1, 3.54, 3.131592, False, 'str-1', [1,4], {11:13, 4.55:14}, ('str-2','str-3')]
for i in my_list_1:
    print(type(i))
# Ручной ввод с ошибкой в определении строки/числа
n = int(input("Введите количество элементов списка: "))
my_list_2 = list(input("Введите первый элемент списка: "))
k = 0
int_1 = 0
float_1 = 0
str_1 = 0
while k < len(my_list_2[0]):
    if my_list_2[0][k] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '.':
        int_1 += 1
    else:
        str_1 += 1
    k += 1
if str_1 == 0:
    if int_1 != 0:
        k = 0
        while k < len(my_list_2[0]):
            if my_list_2[0][k] == '.':
                float_1 = 1
            k += 1
        if float_1 == 1:
            my_list_2[0] = float(my_list_2[0])
        else:
            my_list_2[0] = int(my_list_2[0])
j = 1
while j<n:
    var = input("Введите элемент списка: ")
    k = 0
    int_1 = 0
    float_1 = 0
    str_1 = 0
    while k<len(var):
        if var[k] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '.':
            int_1 += 1
        else:
            str_1 += 1
        k += 1
    if str_1 == 0:
        if int_1 != 0:
            k = 0
            while k < len(var):
                if var[k] == '.':
                    float_1 = 1
                k += 1
            if float_1 == 1:
                var = float(var)
            else:
                var = int(var)
    my_list_2.append(var)
    j += 1
for j in my_list_2:
    print(type(j))
