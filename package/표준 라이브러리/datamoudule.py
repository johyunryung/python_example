from datetime import datetime

print('현재 날짜 시각 객체 얻기' )
today = datetime.now()
print(today)
print(today.year , today.month, today.day, today.hour, today.minute, today.second, today.weekday())

day = datetime(1991, 11, 18 , 0 , 0, 0)
day = datetime(2004, 6, 15 , 0 , 0, 0)
day = datetime(2020, 12, 25 , 0 , 0, 0)
day = datetime(2020, 12, 3 , 0 , 0, 0)
day = datetime(2021, 5, 3 , 0 , 0, 0)
print(today - day)
