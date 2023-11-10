
# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
fields = ['Фамилия', "Имя", "Телефон", "Описание"]
def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии ',
          '3. Изменить номер телефона ',
          '4. Удалить запись ',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу',
          '8. Копировать данные', sep='\n')
    try:
        choice = int(input())
    except ValueError:
        choice = 1
    except KeyboardInterrupt:
        choice = 7
    return choice


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.csv')
    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name=input('lastname ')
            find_by_lastname(phone_book, last_name)
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            lastname = input('lastname ')
            delete_by_lastname(phone_book, lastname)
        elif choice == 5:
            number = input('number ')
            find_by_number (phone_book, number)
        elif choice == 6:
            user_data = input('new data ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 8:
            string_number = int(input('номер строки для копирования '))
            file_name = input('имя файла в который копировать ')
            copy_data_to_other_file(file_name, string_number, phone_book)

        choice = show_menu()
def copy_data_to_other_file(file_name, string_number, phone_book):
    try:
        write_txt(file_name, [phone_book[string_number]])
    except IndexError:
        print("строка", string_number, "отсутствует в справочнике")

def read_txt(filename):
    phone_book = []
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(list(zip(fields, line.split(','))))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    print(phone_book)
    print(filename)
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s += v+','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    head = ""
    delimiter = 15
    for i in fields:
        head += i
        for d in range(delimiter - len(i)):
            head +=" "
    print(head)
    for i in phone_book:
        s = ""
        for j in i.values():
            s += j
            for d in range(delimiter - len(j)):
                s += " "
        print(s[:-2])
    print()

def find_by_lastname(phone_book,last_name):
    error = True
    for i in phone_book:
        if i["Фамилия"] == last_name is not None:
            error = False
            print(last_name, i["Телефон"])
    if error:
        print(last_name, "нет в справочнике")
    print()

def change_number(phone_book, last_name, new_number):
    error = True
    for i in phone_book:
        if i["Фамилия"] == last_name is not None:
            error = False
            i["Телефон"] = new_number
    if error:
        print(last_name, "нет в справочнике")

def delete_by_lastname(phone_book,last_name):
    error = True
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] == last_name is not None:
            phone_book.pop(i)
            break
    if error:
        print(last_name, "нет в справочнике")

def find_by_number (phone_book, number):
    error = True
    for i in phone_book:
        if i["Телефон"] == number is not None:
            error = False
            print(i["Фамилия"])
    if error:
        print(number, "нет в справочнике")

def add_user(phone_book, user_data):
    record = dict(list(zip(fields, user_data.split(','))))
    phone_book.append(record)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    work_with_phonebook()

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
