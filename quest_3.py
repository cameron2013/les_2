# Третье задание
# Времена года через список
part_year = ['Зима', 'Весна', 'Лето', 'Осень','Зима']
n = int(input("Ввелите номер месяца: "))
print(part_year[n//3])

# Времена года через словарь
part_year_dict = {1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень',5:'Зима'}
print(part_year_dict.get(n//3+1))

# Месяцы через список
month = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
print(month[n-1])

# Месяцы через словарь
month_dict = {1:'Январь',2:'Февраль',3:'Март',4:'Апрель',5:'Май',6:'Июнь',7:'Июль',8:'Август',9:'Сентябрь',10:'Октябрь',11:'Ноябрь',12:'Декабрь'}
print(month_dict.get(n))
