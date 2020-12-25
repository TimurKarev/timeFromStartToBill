from datetime import datetime
from dateutil.rrule import rrule, DAILY, TU, MO, TH, FR, WE
from dateutil.relativedelta import relativedelta
#import holidays

HOLIDAYS_2020 = [
    datetime(2020, 1, 1),
    datetime(2020, 1, 2),
    datetime(2020, 1, 3),
    datetime(2020, 1, 6),
    datetime(2020, 1, 7),
    datetime(2020, 1, 8),
    datetime(2020, 2, 24),
    datetime(2020, 3, 9),
    datetime(2020, 5, 1),
    datetime(2020, 5, 4),
    datetime(2020, 5, 5),
    datetime(2020, 5, 11),
    datetime(2020, 6, 12),
    datetime(2020, 11, 4),
]

def get_working_days_from_two_datetime(start_date, end_date, years = [2020]) -> int:
    """Возвращает количество рабочих дней по двум datetime"""
    ru_holidays = HOLIDAYS_2020
    wd = 0

    if start_date > end_date:
        return -1

    for dt in rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(TU, TH, MO, FR, WE)):
        if dt not in ru_holidays:
            wd += 1
    return wd
