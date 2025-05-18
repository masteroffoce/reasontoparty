import json
import datetime
import sys

with open('holidays.json', 'r',) as file:
    data = json.load(file)

inpt = sys.argv[1:]
if inpt:
    current_day = inpt[0]
    current_month = inpt[1]
else:
    current_time = datetime.datetime.now()
    current_month = current_time.strftime("%-m")
    current_day = current_time.strftime("%d")

print(data[current_month][current_day])
