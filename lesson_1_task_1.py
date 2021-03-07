"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.

!!! делал по заданию с сайта, в методичке чуть изменены условия
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Но считаю задание полностью выполненным
"""

while True:
    try:
        duration = int(input('Введите кол-во секунд: '))
        break
    except ValueError:
        print('Вы указали не целое число')

minute = 60
hour = minute * 60
day = hour * 24
month = day * 30
year = month * 12

sec_text = 'сек'
min_text = 'мин'
hour_text = 'час'
day_text = 'дн'
month_text = 'мес'

# по сути эта переменная лишняя, но я ее добавляю для единообразия переменных
# посчитал, что назвать duration сразу duration_seconds нельзя, по требованию задачи
duration_seconds = duration

duration_minutes = duration_seconds // minute
duration_minutes_seconds_rest = duration_seconds % minute

duration_hours = duration_seconds // hour
duration_hours_minutes_rest = int((duration_seconds % hour) / minute)

duration_days = duration_seconds // day
duration_days_hours_rest = int((duration_seconds % day) / hour)

duration_months = duration_seconds // month
duration_months_days_rest = int((duration_seconds % month) / day)

duration_years = duration_seconds // year
duration_years_months_rest = int((duration_seconds % year) / month)

# сначала хотел попрятать дубли в переменные, но потом понял
# что будет сложнее читаться
if duration < minute:
      print(f'{duration_seconds} {sec_text}')
elif minute <= duration < hour:
      print(f'{duration_minutes} {min_text}',
            f'{duration_minutes_seconds_rest} {sec_text}')
elif hour <= duration < day:
      print(f'{duration_hours} {hour_text}',
            f'{duration_hours_minutes_rest} {min_text}',
            f'{duration_minutes_seconds_rest} {sec_text}')
elif day <= duration < month:
      print(f'{duration_days} {day_text}',
            f'{duration_days_hours_rest} {hour_text}',
            f'{duration_hours_minutes_rest} {min_text}',
            f'{duration_minutes_seconds_rest} {sec_text}')
elif month <= duration < year:
      print(f'{duration_months} {month_text}',
            f'{duration_months_days_rest} {day_text}',
            f'{duration_days_hours_rest} {hour_text}',
            f'{duration_hours_minutes_rest} {min_text}',
            f'{duration_minutes_seconds_rest} {sec_text}')
elif duration >= year:
      grp_1 = ('1', '2', '3', '4')
      duration_years_str = str(duration_years)
      if duration_years_str.endswith(grp_1):
            year_text = 'год'
      else:
            year_text = 'лет'

      print(f'{duration_years} {year_text}',
            f'{duration_years_months_rest} {month_text}',
            f'{duration_months_days_rest} {day_text}',
            f'{duration_days_hours_rest} {hour_text}',
            f'{duration_hours_minutes_rest} {min_text}',
            f'{duration_minutes_seconds_rest} {sec_text}')
