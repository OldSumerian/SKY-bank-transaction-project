# Курсовая работа №3 (основы Backend-разработки)
# выполнена Щемеровым С.А. (профессия "Backend-разработчик" 38IND)

#Импортируем библиотеки для работы с файлом json содержащим данные для обработки программой
import json
import sys
import os


def get_info_from_json():
    """
    Получает данные из json файла
    :return:
    """
    script_dir = os.path.dirname(sys.argv[0])
    with open(os.path.join(script_dir, 'operations.json'), 'rt') as oper:
        data = json.load(oper)
    return data


def get_5_last_executed_operation(data_from_json_list):
    """
    Отбирает из полученных данных пять последних выполненных операций и возвращает их в виде списка словарей
    :param data_from_json_list:
    :return:
    """
    data = data_from_json_list[::-1]
    count = 0
    executed_operations = []
    for i in data:
        for key, value in i.items():
            if key == 'state' and value == 'EXECUTED':
                executed_operations.append(i)
                count += 1
                if count == 5:
                    return executed_operations


def check_and_autofill_data_in_executed_operations(executed_operation_list):
    """
    Функция запускает последовательность функций по обработке полученных данных
    о пяти последних операциях клиента для последующего вывода в требуемом формате
    :param executed_operation_list:
    :return:
    """
    format_date(executed_operation_list)
    is_data_in_operation_list(executed_operation_list)
    format_data_in_from(executed_operation_list)
    format_data_in_to(executed_operation_list)
    return executed_operation_list


def format_date(executed_operation_list):
    """
    Функция проверяет значение даты проведения операции на истинность (не пустое значение)
    и переводит данное значение в требуемый формат
    :param executed_operation_list:
    :return:
    """
    for i in executed_operation_list:
        if i['date']:
            i['date'] = i['date'][8:10] + '.' + i['date'][5:7] + '.' + i['date'][:4]
    return executed_operation_list


def is_data_in_operation_list(executed_operation_list):
    """
    Функция проверяет наличие значений у позиций, подлежащих выводу
    и при их отсутствии присваивает значение информационного характера
    об отсутствии требуемых данных
    :param executed_operation_list:
    :return:
    """
    for i in executed_operation_list:
        if 'date' not in i.keys():
            i['date'] = 'данных о дате нет'
        if 'description' not in i.keys():
            i['description'] = 'сведений об описании операции нет'
        if 'from' not in i.keys():
            i['from'] = 'неизвестный номер карты/счета списания'
        if 'to' not in i.keys():
            i['to'] = 'сведения о счете/карте зачисления отсутствуют'
    return executed_operation_list


def format_data_in_from(executed_operation_list):
    """
    Функция проверяет тип исходящей банковской операции (со счета или карты)
    и приводит значение в формат подлежащий выводу на печать
    :param executed_operation_list:
    :return:
    """
    for i in executed_operation_list:
        if 'счет' in i['from'].lower():
            i['from'] = '**' + i['from'][-4:]
        elif 'МИР' in i['from'] or 'Maestro' in i['from'] or 'Visa' in i['from']:
            card = i['from'].split()
            num = card.pop()
            name = ' '.join(card)
            i['from'] = f"{name} {num[:4]} {num[4:6]}** **** {num[-4:]}"
    return executed_operation_list


def format_data_in_to(executed_operation_list):
    """
    Функция проверяет тип входящей банковской операции (на счет или карту)
    и приводит значение в формат подлежащий выводу на печать
    :param executed_operation_list:
    :return:
    """
    for i in executed_operation_list:
        if 'счет' in i['to'].lower():
            i['to'] = '**' + i['to'][-4:]
        elif 'МИР' in i['to'] or 'Maestro' in i['to'] or 'Visa' in i['to']:
            card = i['to'].split()
            num = card.pop()
            name = ' '.join(card)
            i['to'] = f"{name} {num[:4]} {num[4:6]}** **** {num[-4:]}"
    return executed_operation_list


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


def main():
    print_info(check_and_autofill_data_in_executed_operations(get_5_last_executed_operation(get_info_from_json())))


if __name__ == '__main__':
    main()
