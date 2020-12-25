from datetime import datetime
import pandas as pd


def clean_multiple_rows(row):
    """ Создает из Серии несколько серий если в ячейке указанно несколько входов
    делавает из строчки date и убирает время """
    _part = row.part_name
    _init = row.initial_date
    _creat = row.creation_date
    _appr = row.approved_date
    _master = row.master_name
    _manager = row.manager_name
    _bill = row.bill_date

    dt_initial_time = get_dt_from_str_list_by_index([_init], 0)
    # print(dt_initial_time)

    creation_list = _creat.splitlines()
    approved_list = _appr.splitlines()
    bill_list = _bill.splitlines()
    master_name_list = _master.splitlines()
    manager_name_list = _manager.splitlines()

    min_div_number = min(
        [
            len(creation_list),
            len(approved_list),
            len(bill_list),
            len(master_name_list),
            len(manager_name_list),
        ]
    )
    part_name = []
    initial_time = []
    creation_time = []
    approved_time = []
    bill_time = []
    master_name = []
    manager_name = []

    for i in range(min_div_number):
        part_name.append(_part.split()[0])
        initial_time.append(dt_initial_time)
        creation_time.append(get_dt_from_str_list_by_index(creation_list, i))
        approved_time.append(get_dt_from_str_list_by_index(approved_list, i))
        bill_time.append(get_dt_from_str_list_by_index(bill_list, i))
        master_name.append(master_name_list[i])
        manager_name.append(manager_name_list[i])

    d = pd.DataFrame(data={
        'part_name': part_name,
        'initial_time': initial_time,
        'creation_time': creation_time,
        'approved_time': approved_time,
        'bill_time': bill_time,
        'master_name': master_name,
        'manager_name': manager_name
    })
    return d


def get_dt_from_str_list_by_index(lst: list, i: int):
    """Возвращает datetime из списка со строками по индексу"""
    return datetime.strptime(lst[i].split()[0][:10], "%d.%m.%Y")
