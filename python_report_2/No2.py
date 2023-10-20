import calendar

print(f"2022년은 윤년? : {calendar.isleap(2022)}")
print(f"2000~2050년 사이의 윤년의 갯수: {calendar.leapdays(2000, 2050)}")
print("2022년 10월 13일은: ", end="")
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
