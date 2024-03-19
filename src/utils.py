# Импортируем библиотеки для работы с файлом json содержащим данные для обработки программой
import json


def get_info_from_json():
    """
    Получает данные из json файла
    :return:
    """
    with open('data/operations.json', encoding='UTF-8') as data:
        all_operations_list = json.load(data)
    return all_operations_list


def get_executed_operation(all_operations_list):
    """
    Функция выбирает из полученных данных только успешные ('EXECUTED') операции
    :param all_operations_list:
    :return:
    """
    executed_operations = []
    for i in all_operations_list:
        if 'state' in i.keys():
            if i['state'] == 'EXECUTED':
                executed_operations.append(i)
    return executed_operations


def get_5_last_operations(executed_operations):
    """
    Функция сортирует полученный список операций по дате и возвращает пять последних по времени
    :param executed_operations:
    :return:
    """
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations[:5]


def format_number(operation_data):
    """
    Функция по шифрованию данных счетов и карт
    :param operation_data:
    :return:
    """
    info = operation_data.split()
    number = info.pop()
    name = ' '.join(info)
    if name.lower() == 'счет':
        return f"{name} **{number[-4:]}"
    else:
        return f"{name} {number[:4]} {number[4:6]}** **** {number[-4:]}"


def check_operations_data(operations_list):
    """
    Функция по проверке наличия корректных ключей в поступившей базе и
    по форматированию содержащихся в базе данных для вывода
    :param operations_list:
    :return:
    """
    for i in operations_list:
        if 'from' in i.keys():
            i['from'] = format_number(i['from'])
        elif 'from' not in i.keys():
            i['from'] = ''
        if 'to' in i.keys():
            i['to'] = format_number(i['to'])
        elif 'to' not in i.keys():
            i['to'] = ''
        if 'date' in i.keys():
            i['date'] = i['date'] = i['date'][8:10] + '.' + i['date'][5:7] + '.' + i['date'][:4]
    return operations_list


def print_info(executed_operations_list):
    """
    Функция выводит на печать отформатированные данные о совершенных банковских операциях
    :param executed_operations_list:
    :return:
    """
    for i in executed_operations_list:
        print(i['date'], i['description'])
        print(f"{i['from']} -> {i['to']}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print()
