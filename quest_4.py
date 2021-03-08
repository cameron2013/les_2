str_1 = input("Введите строку: ")
str_list = str_1.split(' ')
for i in range(len(str_list)):
    if len(str_list[i])<=10:
        print(f"{i+1} {str_list[i]}")
    else:
        print(f"{i + 1} {str_list[i][0:10]}")
