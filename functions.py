from data_base import list_view, write_data, write_data1, write_read_csv
from pathlib import Path


def func_1():
    print(list_view())


def func_2():
    add_rec1 = str(input('Введите фамилию абонента: '))
    add_rec2 = str(input('Введите имя абонента: '))
    add_rec3 = str(input('Введите номер телефона абонента: '))
    write_data(add_rec1, add_rec2, add_rec3)
    print('Добавлен абонент:', add_rec1, ' ', add_rec2, ' ', add_rec3)


def func_3():
    del_rec = str(input('Введите фамилию или имя или номер абонента: '))
    a = list_view().split()
    if del_rec not in a:
        print('Такой записи нет в тел книге')
        func_3()
    else:
        index = a.index(del_rec)
        if (index-1) % 3 == 0 or index == 1:
            del a[index+1]
            del a[index]
            del a[index-1]
        elif index == 0 or index % 3 == 0:
            del a[index+2]
            del a[index+1]
            del a[index]
        elif index != 0 or (index + 1) % 3 == 0:
            del a[index]
            del a[index-1]
            del a[index-2]
    z = len(a)
    d = Path('Phonebook.txt')
    with open(d, 'w', encoding="utf-8") as data:
        data.seek(0)
        data.truncate()
    while z != 0:
        write_data1(a[0], a[1], a[2])
        del a[:3]
        z = z - 3
    print('Абонент удален')


def func_4():
    a = list_view().split()
    edit_line = str(
        input('Введите фамилию или имя или телефон абонента для редактирования записи: '))
    if edit_line not in a:
        print('Такой записи нет в тел книге')
        func_4()
    else:
        index = a.index(edit_line)
        if (index-1) % 3 == 0 or index == 1:
            print(a[index-1], ' ', a[index], ' ', a[index+1])
            add_rec = list(map(str,
                               input('Введите исправленные фамилию, имя и телефон через пробел:').split()))
            del a[index+1]
            del a[index]
            del a[index-1]
        elif index == 0 or index % 3 == 0:
            print(a[index], ' ', a[index+1], ' ', a[index+2])
            add_rec = list(map(str,
                               input('Введите исправленные фамилию, имя и телефон через пробел:').split()))
            del a[index+2]
            del a[index+1]
            del a[index]
        elif index != 0 or (index + 1) % 3 == 0:
            print(a[index-2], ' ', a[index-1], ' ', a[index])
            add_rec = list(map(str,
                               input('Введите исправленные фамилию, имя и телефон через пробел:').split()))
            del a[index]
            del a[index-1]
            del a[index-2]
    b = a + add_rec
    z = len(b)
    d = Path('Phonebook.txt')
    with open(d, 'w', encoding="utf-8") as data:
        data.seek(0)
        data.truncate()
    while z != 0:
        write_data1(b[0], b[1], b[2])
        del b[:3]
        z = z - 3
    print('Данные абонента: ', edit_line,
          'заменены на: ', str(' '.join(add_rec)))


def func_5():
    a = list_view().split()
    find_line = str(
        input('Введите фамилию или имя или телефон абонента для поиска записи: '))
    if find_line not in a:
        print('Такой записи нет в тел книге')
        func_5()
    else:
        index = a.index(find_line)
        if (index-1) % 3 == 0 or index == 1:
            print(a[index-1], ' ', a[index], ' ', a[index+1])
        elif index == 0 or index % 3 == 0:
            print(a[index], ' ', a[index+1], ' ', a[index+2])
        elif index != 0 or (index + 1) % 3 == 0:
            print(a[index-2], ' ', a[index-1], ' ', a[index])


def func_6():
    write_read_csv()
