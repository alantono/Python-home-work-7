from pathlib import Path


def list_view():
    d = Path('Phonebook.txt')
    with open(d, 'r', encoding="utf-8") as data:
        return data.read()


def write_data(add_rec1, add_rec2, add_rec3):
    d = Path('Phonebook.txt')
    with open(d, 'a', encoding="utf-8") as data:
        a = f"{add_rec1}\n{add_rec2}\n{add_rec3}\n"
        data.writelines(a)


def write_data1(surname, name, number):
    d = Path('Phonebook.txt')
    with open(d, 'a', encoding="utf-8") as data:
        a = f"{surname}\n{name}\n{number}\n\n"
        data.write(a)


def write_read_csv():
    import csv
    a = list(list_view().split())
    z = len(a)
    with open('Phonebook.csv', 'w', newline='', encoding="utf-8") as data:
        csvwriter = csv.writer(data, delimiter=';')
        csvwriter.writerow(['Фамилия'] + ['Имя'] + ['Номер'])
        while z != 0:
            csvwriter.writerow([a[0], a[1], a[2]])
            del a[:3]
            z = z - 3
    with open('Phonebook.csv', 'r', newline='', encoding="utf-8") as data:
        csvreader = csv.reader(data)
        for row in csvreader:
            print(', '.join(row))
