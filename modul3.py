# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)


# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)


# from datetime import datetime

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime

# #----------------------------------strftime--------------------------->
# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"{formatted_date} - type: {type(formatted_date)}") 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)
# #<---------------------------------strftime---------------------------

# #----------------------------------strptime--------------------------->
# from datetime import datetime

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(formatted_date, "%Y-%m-%d %H:%M:%S")
# print(print(f"{datetime_object} - type: {type(datetime_object)}"))  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
# #<----------------------------------strptime---------------------------
from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  

#<----------------------------------Робота з ISO8601 форматом дати---------------------------

from datetime import datetime

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_date_string = now.isoformat()
print(f"{iso_date_string} - string")

from datetime import datetime

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(f"{date_from_iso} - object datetime")

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(iso_calendar)
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)
#<----------------------------------Робота з ISO8601 форматом дати---------------------------


#----------------------------------TIME----------------------------------------------------->
import time

print(f"Поч. паузи- {time.ctime(time.time())}")
time.sleep(5)
print(f"Кін. паузи- {time.ctime(time.time())}")

import time

current_time = time.time() 
print(f"Поточний час: {current_time} (поточний час у секундах з 1 січня 1970 року (epoch time))")                     #час від 01.01.1970

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")


import time

current_time = time.time()
print(f"Поточний час: {current_time}")

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")

utc_time = time.gmtime(current_time)
print(f"UTC час: {utc_time}")


import time

# Записуємо час на початку виконання
start_time = time.perf_counter()
print(start_time)
# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()
print(end_time)
# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

#<---------------------------------TIME------------------------------------------------------