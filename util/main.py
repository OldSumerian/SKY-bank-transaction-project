# Курсовая работа №3 (основы Backend-разработки)
# выполнена Щемеровым С.А. (профессия "Backend-разработчик" 38IND)

import json


def get_info_from_json():
    """
    Получает данные из json файла
    :return:
    """
    with open('operations.json') as oper:
        oper_full_info = json.loads(oper.read())
        return oper_full_info


print(get_info_from_json())
