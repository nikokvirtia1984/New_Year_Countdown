from datetime import datetime, timedelta
import time

while True:
    date_now = datetime.today()
    date_now_timestamp = int(date_now.timestamp())
    new_year_date = datetime(year=date_now.year + 1, month=1, day=1, hour=0, minute=0, second=0)
    new_year_timestamp = int(new_year_date.timestamp())
    remaining_time_seconds = new_year_timestamp - date_now_timestamp

    remaining_time = timedelta(seconds=remaining_time_seconds)
    remaining_day = remaining_time.days
    remaining_seconds = remaining_time.seconds

    remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
    remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)

    if remaining_day:
        if remaining_day > 1:
            remaining_day = f'{remaining_day} Days'
        else:
            remaining_day = f'{remaining_day} Day'
    else:
        remaining_day = '0'

    if remaining_hours:
        if remaining_hours > 1:
            remaining_hours = f'{remaining_hours} Hours '
        else:
            remaining_hours = f'{remaining_hours} Hour'
    else:
        remaining_hours = '0'

    if remaining_minutes:
        if remaining_minutes > 1:
            remaining_minutes = f'{remaining_minutes} Minutes'
        else:
            remaining_minutes = f'{remaining_minutes} Minute'
    else:
        remaining_minutes = '0'

    if remaining_seconds:
        if remaining_seconds > 1:
            remaining_seconds = f'{remaining_seconds} Seconds'
        else:
            remaining_seconds = f'{remaining_seconds} Second'
    else:
        remaining_seconds = '0'

    print(f'\r{remaining_day} {remaining_hours} {remaining_minutes} {remaining_seconds} Left till New Year', end='')
    time.sleep(1)
