# Пятое задание
list_range = [7, 5, 4, 4, 2]
while True:
    a = int(input("Введите номер рейтинга: "))
    t = False
    r = False
    for i in range(len(list_range)):
        if a == list_range[i]:
            t = True
    if t:
        list_range.insert(list_range.index(a) + list_range.count(a), a)
    if not t:
        for i in range(len(list_range)):
            if a > list_range[i]:
                list_range.insert(i, a)
                break
            if i == len(list_range) - 1:
                list_range.append(a)
    print(list_range)
    b = input("Новое значение рейтинга? Да - любое, Нет - 0: ")
    if b == '0':
        break
