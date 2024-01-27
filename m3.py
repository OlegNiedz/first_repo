#---------------task_1--------------
import random
import re
from datetime import datetime as dtdt, timedelta

strdate = '2020-10-09'

def get_days_from_today(strdate):
    obj_date = dtdt.strptime(strdate, '%Y-%m-%d').toordinal()
    curday = dtdt.today().toordinal()
    return curday-obj_date
   
print(f"\n-------------------Task1-----------------\nВід дати {strdate} минуло {get_days_from_today(strdate)} днів")

#---------------task_2--------------


def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000 or quantity not in range(min,max+1):
        return ""
    winlist = []
    while len(winlist)<quantity:
        a=random.randint(min,max)
        if a not in winlist:
            winlist.append(a)
            winlist.sort()
    return winlist
   
print(f"\n-------------------Task2-----------------\nВиграшні лотерейні числа (5 з 36):{get_numbers_ticket(1,36,5)}")
print(f"Виграшні лотерейні числа (6 з 49):{get_numbers_ticket(1,49,6)}")

#---------------task_3-------------

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern=r"[\d\+]+"
    phone_number="".join(re.findall(pattern, phone_number))
    correct=""
    match len(phone_number):
        case 9:correct="+380"
        case 10:correct="+38"
        case 11:correct="+3"
        case 12:correct="+"
    return correct+phone_number
print("\n-------------------Task3-----------------")
for phone_number in raw_numbers:
    print(normalize_phone(phone_number))


#---------------task_4-------------

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Semen Petrenko", "birthday": "1990.02.25"}
]

def get_upcoming_birthdays(users):
    today = dtdt.today().date()
    upcoming_birthdays=[]
    for user in users:
        strBirthday = user["birthday"]
        if int(strBirthday[5:7])<today.month:
            strBirthday = str(today.year+1)+strBirthday[4:]
        else:
            strBirthday = str(today.year)+strBirthday[4:]
        birthday = dtdt.strptime(strBirthday,'%Y.%m.%d').date()
        dDays = (birthday - today).days
        if 0<=dDays<7:  
            match birthday.weekday():
                case 5: birthday=birthday.__add__(timedelta(days=2))
                case 6: birthday=birthday.__add__(timedelta(days=1))
            upcoming_birthdays.append({'name':user["name"],'congratulation_date':dtdt.strftime(birthday,'%Y.%m.%d')})
              
    return upcoming_birthdays

print(f"\n-------------------Task4-----------------\n{get_upcoming_