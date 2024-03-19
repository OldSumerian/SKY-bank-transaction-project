import src.utils


def test_get_executed_operation(data_for_test):
    assert len(src.utils.get_executed_operation(data_for_test)) == 6
    assert src.utils.get_executed_operation(data_for_test)[0]['state'] == 'EXECUTED'


def test_get_5_last_operations(data_for_test):
    assert src.utils.get_5_last_operations(data_for_test)[0]['date'] == "2019-08-26T10:50:58.294041"
    assert len(src.utils.get_5_last_operations(data_for_test)) == 5


def test_format_number(data_for_test):
    assert src.utils.format_number(data_for_test[0]['from']) == "Maestro 1596 83** **** 5199"
    assert src.utils.format_number(data_for_test[-1]['to']) == "Счет **8612"



def test_check_operations_data(data_for_test):
    assert src.utils.check_operations_data([]) == []
    assert src.utils.check_operations_data(data_for_test)[0]['date'] == '26.08.2019'

