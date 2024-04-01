from datetime import datetime
from datetime import timedelta

def date_generator(start, end, step):
    while start <= end:
        yield start                  # Возвращаем текущую дату
        start += step  

def interval_generator(start_date, end_date, state):
    if state == 0:
        step = timedelta(minutes=1)
    elif state == 1:
        step = timedelta(hours=1)
    elif state == 2:
        step = timedelta(days=1)
    elif state == 3:
        step = timedelta(weeks=1)

    # dates = []
    # times = []
    datetime_array = []

    for single_date in date_generator(start_date, end_date, step):
        datetime_array.append([single_date.strftime("%d/%m/%Y"), single_date.strftime("%H:%M:%S")])
        # print([single_date.strftime("%d/%m/%Y"), single_date.strftime("%H:%M")]) 

    # print(datetime_array)

    return datetime_array

# print(interval_generator())