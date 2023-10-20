import calendar

print(calendar.isleap(2022))
print(calendar.leapdays(2000, 2050))
match calendar.weekday(2022, 10, 13):
    case 0:
        print("월요일")
    case 1:
        print("화요일")
    case 2:
        print("수요일")
    case 3:
        print("목요일")
    case 4:
        print("금요일")
    case 5:
        print("토요일")
    case 6:
        print("일요일")
