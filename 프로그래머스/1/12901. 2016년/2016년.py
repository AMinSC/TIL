def solution(a, b):
    import calendar
    week = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
    return week[calendar.weekday(2016, a, b)]