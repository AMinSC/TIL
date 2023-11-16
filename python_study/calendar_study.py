import calendar

print(calendar.calendar(2016))

weekday_dict = {0: "월", 1:"화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

print("2016년 11월 3일은 무슨 요일인가?", weekday_dict[calendar.weekday(2016, 11, 3)])
