import datetime
import json
import sys

with open('weekday.json', 'r') as file:
    data = json.load(file)

inpt = sys.argv[1:]
if inpt:
    current_day = datetime.datetime(int(inpt[2]), int(inpt[1]), int(inpt[0]))
else:
    current_day = datetime.datetime.now()
day = int(current_day.strftime("%d"))
month = current_day.strftime("%-m")
ordinality = -(-day//7)
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weekday = weekdays.index(current_day.strftime("%a")) + 1

try:
    holiday = data[month][str(ordinality)][str(weekday)]
except:
    holiday = ''

months_lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(current_day.strftime("%Y"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            months_lengths[1]=29
    else:
        months_lengths[1]=29

if day + 7 > months_lengths[int(month)-1]:
    try:
        holiday = data[month]["-1"][str(weekday)]
    except:
        holiday = holiday
print(holiday)
