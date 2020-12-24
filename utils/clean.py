from datetime import datetime


def clean_multiple_rows(row):
    """ Создает из Серии несколько серий если в ячейке указанно несколько входов
    делавает из строчки date и убирает время """
    part_name = row.part_name
    initial = row.initial_date
    creation = row.creation_date
    approved = row.approved_date
    master_name = row.master_name
    manager_name = row.master_name
    bill = row.master_name

    dt_initial_time = datetime.strptime(initial.split()[0][:10], "%d.%m.%Y")
    #print(dt_initial_time)

    i1 = len(creation.splitlines())
    i2 = len(approved.splitlines())
    i3 = len(bill.splitlines())
    i4 = len(master_name.splitlines())
    i5 = len(manager_name.splitlines())

    if i1 == i2 == i3 == i4 == i5:
        return True

    return False

