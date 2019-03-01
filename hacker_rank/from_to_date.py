##
# Python's program to print all Monday's of a specific year
 
from datetime import date, timedelta
from datetime import datetime
import requests
import json

days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
year = 2017
date_object = date(year, 1, 2)
print(date_object)
print(date_object.day)
print(date_object.month)
print(date_object.strftime("%s"))
date_object += timedelta(days=0)
date_object_2 = date(year, 1, 30)
while date_object != date_object_2: 
#while date_object.year != 2018:
    print(date_object)
    print(date_object.strftime("%s"))
    #print(days[date.weekday(date_object)])
    date_object += timedelta(days=7)

r = requests.get('https://jsonmock.hackerrank.com/api/stocks')
data = r.json()
if 'data' in data:
    data = data['data']
for one in data:
    test_date = (one['date'])
    datetimeObj = datetime.strptime(one['date'], '%d-%B-%Y')
 #   test_date_ll = test_date.split("-")
 #   test_date_obj = date(int(test_date_ll[2]), int(test_date_ll[0]), test_date_ll[1])
 #   time_stamp_3 = test_date_obj.strftime("%s")
    print(date.weekday(datetimeObj))
    print(datetime.timestamp(datetimeObj))
