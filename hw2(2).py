import csv


def greet():
    """Приветствует пользователя и выводит меню"""
    print('Выберите пункт меню и введите соответствующее число')
    print('1. Вывести в виде иерархию команд')
    print('2. Вывести сводный отчёт по департаментам')
    print('3. Сохранить сводный отчёт в виде csv-файла')
    answer = input()
    if answer == '1':
        return first_point()
    elif answer == '2':
        return second_point()
    elif answer == '3':
        return third_point()
    else:
        print('Ошибка! Введите число корректно')
        greet()


def open_csv():
    """Открывает файл и превращает его во вложенный список"""
    corp_summary = []
    with open('Corp_Summary (1).csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            row_list = []
            for element in row:
                row_list.append(element)
            corp_summary.append(row_list)
    return corp_summary


def first_point():
    """Выводит иерархию команд"""
    lst = open_csv()[1:]
    dep_com = {}
    for element in lst:
        try:
            if element[2] not in dep_com[element[1]]:
                dep_com[element[1]].append(element[2])
        except KeyError:
            dep_com[element[1]] = [element[2]]
    print(dep_com)
    return dep_com


def second_point():
    """Выводит сводный отчет по департаментам"""
    lst = open_csv()[1:]
    final = [['Название', 'Численность', 'Вилка ЗП', 'Средняя ЗП']]
    for element in lst:
        flag = False
        for element_final in final:
            if element[1] == element_final[0]:
                element_final[1] += 1
                element_final[2].append(int(element[5]))
                element_final[3].append(int(element[5]))
                flag = True
        if flag is False:
            final.append([element[1], 1, [int(element[5])],  [int(element[5])]])
    for i in range(1, len(final)):
        final[i][3] = round(sum(final[i][3])/len(final[i][3]), 2)
        final[i][2] = max(final[i][2]) - min(final[i][2])
    return final


def third_point():
    """Сохраняет сводный отчет в файл"""
    summary = second_point()
    with open('somefile.csv', 'w', encoding='utf8') as csv_out:
        writer = csv.writer(csv_out)
        rows = summary
        writer.writerows(rows)


if __name__ == '__main__':
    greet()
