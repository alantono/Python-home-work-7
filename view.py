def menu():
    print('''Команды для работы c телефонной книгой:
    - Просмотр всей тел книги: 1
    - Добавление новой записи: 2
    - Удаление записи тел книги по фамилии или имени: 3
    - Изменение записи в тел книге: 4
    - Поиск по тел книге: 5
    - Экспорт тел книги в csv файл: 6''')


def get_num():
    num = int(input('Введите команду(от 1 до 6): '))
    return num
