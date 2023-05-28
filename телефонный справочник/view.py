def user_input():
    ask = int(input("Выбери ниже: \n 1 - записать пользователя \n 2 - поиск по имени \n 3 - сортировка по телефону \n "
                    "4 - вывод имен сотрудников \n 5 - вывод всей базы \n 6 - изменить телефон абонента \n "
                    "7 - удалить абонента \n 8 - выход \n"))
    return ask

def people():
    data = list()
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    father = input("Введите отчество: ")
    birthdey = input("Введите дату рождения: ")
    telephone = input("Введите телефон: ")
    data = name + '; ' + family + '; ' + father + '; ' + birthdey + '; ' + telephone + '; ' + '\n'
    #data = d.split(';')'\n'
    return data

def search_people_name():
    str_search = input("Введите имя для поиска: ")
    return str_search


