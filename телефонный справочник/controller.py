import view
import database

def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            data = view.people()
            database.add_data(data)
        elif ask == 2:
            name = view.search_people_name()
            d = database.search_name(name)
        elif ask == 3:
            database.sort_telephon()
        elif ask == 4:
            database.prin_name()
        elif ask == 5:
            database.print_all_base()
        elif ask == 6:
            name = view.search_people_name()
            database.search_name(name)
            database.del_telephon_name(name)
        elif ask == 7:
            name = view.search_people_name()
            database.search_name(name)
            database.del_name(name)
        else:
            ask == 8
            break



main()