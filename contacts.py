import os

phonebook = 'phonebook.txt'


def add_new_contact(contact):
    with open(phonebook, 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(f"{value};")
        file.write('\n')


def ask_data():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    
    contact = {'last_name': last_name,
               'first_name': first_name,
               'middle_name': middle_name,
               'phone_number': phone_number}
    return contact


def show_menu():
    print('''Выберете что хотите сделать:\n1. Список всех контактов\n2. Добавить\n3. Найти\n4. Удалить\n5. Копировать\n0. Выход''')


def show_contacts():
    title = ['Фамилия','Имя','Отчество','Телефон']
    with open(phonebook, 'r', encoding='utf-8') as file:
        print('\t\t'.join(title))
        for line in file:
            print('\t\t'.join(line.split(';')))


def find_contact():
    print('Поиск по:\n1. фамилии\n2. имени\n3. отчеству\n4. номеру')
    search_str = ''
    command = int(input('Введите тип поиска: '))
    if command == 1:
        search_str = input('Введите фамилию: ')
    elif command == 2:
        search_str = input('Введите имю: ')
    elif command == 3:
        search_str = input('Введите отчество: ')
    
    title = ['Фамилия','Имя','Отчество','Телефон']
    with open(phonebook, 'r', encoding='utf-8') as file:
        print('\t\t'.join(title))
        for counter, line in enumerate(file):
            line = line.split(';')
            if search_str in line[command-1]:
                print('\t\t'.join(line))


def delete_contact():
    title = ['Id','Фамилия','Имя','Отчество','Телефон']
    print('\t\t'.join(title))
    
    contacts = get_contacts()
    print_contacts(contacts)

    id_to_delete = int(input('Выберете Id контакта для удаления: '))
    for i in range(len(contacts)):
        if i == id_to_delete:
            contacts.remove(contacts[i])
            print('\t\t'.join(contacts[i].split(';')),' был удален')

    save_changes = input('Хотите ли сохранить изменения в файле контактов?(y/n): ')
    if save_changes.lower() == 'y':
        save_contacts(contacts, phonebook)


def get_contacts():
    contacts = list()
    with open(phonebook, 'r', encoding='utf-8') as file:
        for line in file:
            contacts.append(line)
    return contacts


def print_contacts(contacts):
    for i in range(len(contacts)):
        print(f'{i}\t\t', '\t\t'.join(contacts[i].split(';')))


def save_contacts(contacts, phonebook):
    with open(phonebook, 'w', encoding='utf-8') as file:
        for value in contacts:
            file.write(value)


def copy_contacts():
    title = ['Id','Фамилия','Имя','Отчество','Телефон']
    print('\t\t'.join(title))
    
    contacts = get_contacts()
    print_contacts(contacts)

    ids_to_copy = input('Перечислите Id контактов, которые хотите скопировать через запятой: ')
    ids_list = [int(id) for id in ids_to_copy.split(',')]
    contacts_list_copy = list()
    for i in range(len(contacts)):
        if i in ids_list:
            contacts_list_copy.append(contacts[i])

    phonebook_name = input('Введите название файла для сохранения выбранных контактов c расширением ".txt": ')
    save_contacts(contacts_list_copy, phonebook_name)


def main():
    isContinue = True
    while isContinue:
        os.system('cls')
        show_menu()
        command = int(input('>'))
        if command == 0:
            isContinue = False
        elif command == 5:
            copy_contacts()
        elif command == 4:
            delete_contact()
        elif command == 3:
            find_contact()
        elif command == 2:
            contact = ask_data()
            add_new_contact(contact)
        elif command == 1:
            show_contacts()

        if command != 0:
            input('Нажмите Enter чтоб продолжить')


if __name__ == '__main__': 
    main()