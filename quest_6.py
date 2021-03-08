i = 0
goods = list()
while True:
    i += 1
    name = input("Введите название товара: ")
    cost = input("Введите цену товара: ")
    count = input("Введите количество товаров: ")
    unit = input("Введите ед. измерения (шт., кг. и др.): ")
    good_char = dict(Название=name, Цена=cost, Количество=count, Ед=unit)
    good = (i, good_char)
    goods.append(good)
    a = input("Ввод нового товара: Да - любое, Нет - 0. ")
    if a == "0":
        break
while True:
    a = input("Что вы ходите узнать? Наим. товаров - 1, Цены - 2, Кол. - 3, Ничего - 0: ")
    if a == "1":
        print("Названия товаров: ")
        for i in goods:
            print(i[1].get('Название'))
    if a == "2":
        print("Цены: ")
        for i in goods:
            print(f"{i[1].get('Название')}: {i[1].get('Цена')}")
    if a == "3":
        print("Количество: ")
        for i in goods:
            print(f"{i[1].get('Название')}: {i[1].get('Количество')} {i[1].get('Ед')}")
    if a == "0":
        break
