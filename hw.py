import shutil
tc = shutil.get_terminal_size().columns
fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
file='phonebook.txt'

def print_result(phone_book2):
    print(f"_"*tc, end='\n\n')
    for i in fields:
        print(f"{i : >{tc/6}}", end='')
    print()
    print(f"_"*tc, end='\n\n')
    for i in phone_book2:
        for j in i.values():
            print(f"{j : >{tc/6}}", end='')
    print(f"_"*tc,sep='\n')
    
def find_by_lastname(phone_book1,last_name):
    search=[]
    for i in phone_book1:
        if last_name in i['Фамилия']:
            search.append(i)
    print_result(search)

def find_by_number(phone_book3,number):
    search=[]
    for i in phone_book3:
        if number in i['Телефон']:
            search.append(i)
    print_result(search)

def add_user(phone_book4):
    s=[None]*len(fields)
    for i in range(len(fields)):
        s[i]=input(f"{fields[i]} ")
        if fields[i] == "Описание":
            s[i]=s[i]+'\n'
    record = dict(zip(fields, s))
    phone_book4.append(record)
    print("Запись добавлена:")
    print_result([record])
    write_txt(file,phone_book4)
    return phone_book4

def change_number(phone_book7,last_name,new_number):
    for i in range(len(phone_book7)):
        if last_name == phone_book7[i]['Фамилия']:
            phone_book7[i]['Телефон'] = new_number
            write_txt(file,phone_book7)
            print("Телефон изменен:")
            print_result([phone_book7[i]])
            return phone_book7
    print(f"Контакт {last_name} не найден !")

def delete_by_lastname(phone_book6,lastname):
    for i in range(len(phone_book6)):
        if lastname == phone_book6[i]['Фамилия']:
            print(f"Контакт {lastname} удален:")
            print_result([phone_book6[i]])
            phone_book6.pop(i)
            write_txt(file,phone_book6)
            return phone_book6
    print(f"Контакт {lastname} не найден !")

def copy_db(phone_book8, filenamenew1):
    write_txt(filenamenew1,phone_book8, 'w+')
    print(f"БД сохранена в файл {filenamenew1}")

# _______________________________________________________________

def show_menu():
    print('1. Распечатать справочник',
    '2. Найти контакт по фамилии',
    '3. Изменить номер телефона',
    '4. Удалить запись',
    '5. Найти абонента по номеру телефона',
    '6. Добавить абонента в справочник',
    '7. Скопировать БД в другой файл',
    '8. Закончить работу', sep = '\n')
    choice=int(input())
    return choice

def work_with_phonebook():
    phone_book = read_txt(file)
    choice=show_menu()
    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия ')
            find_by_lastname(phone_book,last_name)
        elif choice==3:
            last_name=input('Фамилия ')
            new_number=input('Новый номер телефона ')
            phone_book=change_number(phone_book,last_name,new_number)
        elif choice==4:
            lastname=input('Фамилия ')
            phone_book=delete_by_lastname(phone_book,lastname)
        elif choice==5:
            number=input('Телефон ')
            find_by_number(phone_book,number)
        elif choice==6:
            phone_book=add_user(phone_book)
        elif choice==7:
            filenamenew=input('Имя нового файла (с расширением) ')
            copy_db(phone_book, filenamenew)
        choice=show_menu()

def read_txt(filename):
    phone_book=[]
    with open(filename,'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
        return phone_book

def write_txt(filename, phone_book, m = 'w'):
    with open(filename,m,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}')
        return True


work_with_phonebook()