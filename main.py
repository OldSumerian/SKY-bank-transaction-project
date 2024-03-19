# Курсовая работа №3 (основы Backend-разработки)
# выполнена Щемеровым С.А. (профессия "Backend-разработчик" 38IND)

# Импортируем функции из файла utils
from src.utils import get_info_from_json, get_executed_operation, get_5_last_operations, check_operations_data
from src.utils import print_info


def main():
    """
    Функция по последовательной обработке данных о банковских операциях, полученных из json-файла
    и их выводу в формате, предусмотренном заданием
    :return:
    """
    data_list = get_info_from_json()
    executed_operations = get_executed_operation(data_list)
    last_5_operations = get_5_last_operations(executed_operations)
    correct_data = check_operations_data(last_5_operations)
    print_info(correct_data)


if __name__ == '__main__':
    main()
