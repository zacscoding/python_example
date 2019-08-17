import calendar

# print(calendar.calendar(2019))

# 3 == 목요일 (월요일 == 0, 일요일 == 6)
print("calendar.weekday(2019, 7, 25) : ", calendar.weekday(2019, 7, 25))

(day, start_day) = calendar.monthrange(2019, 7)
print("> day of 1: %s | start day : %s" % (day, start_day))
