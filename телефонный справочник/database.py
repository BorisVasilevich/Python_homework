def add_data(data):
    with open('baseTelephons.txt', 'a') as file:
        file.writelines(data)
    print("Телефонная книга обновлена!")

def search_name(name):
    with open('baseTelephons.txt', 'r') as file:
        data = file.readlines()
        flag = False
        for i in data:
            if name in i:
                print(i)
                flag = True
        if flag == False:
            print("Абонета нет!")

def sort_telephon():
    with open('baseTelephons.txt', 'r') as file:
        data = file.readlines()
        data.sort(key = lambda x: (x.split(';')[4]))
    with open('baseTelephons.txt', 'w') as file:
        file.writelines(data)

def prin_name():
    with open('baseTelephons.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            print(i.split(';')[0])

def print_all_base():
    with open('baseTelephons.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            print(i)
def del_telephon_name(name):
    with open('baseTelephons.txt', 'r') as file:
        old_data = file.readlines()
        for i in range(len(old_data)):
            if name in old_data[i]:
                a = i
    old_data[a].split(';')[4] = input("Введите новый номер: ")
    new_data = old_data
    with open('baseTelephons.txt', 'w') as file:
        file.writelines(new_data)

def del_name(name):
    with open('baseTelephons.txt', 'r') as file:
        old_data = file.readlines()
        for i in range(len(old_data)):
            if name in old_data[i]:
                a = i
    del old_data[a]
    new_data = old_data
    with open('baseTelephons.txt', 'w') as file:
        file.writelines(new_data)