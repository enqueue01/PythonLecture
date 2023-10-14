def get_dest(location):
    return dest_dict.get(location)


def get_class(class_type):
    return class_dict.get(class_type)


def get_seat(seat_type):
    return seat_dict.get(seat_type)


dest_dict = {
    "춘천": 5000,
    "부산": 30000,
    "대구": 20000,
    "수원": 10000
}

class_dict = {
    "KTX": 10000,
    "새마을호": 5000,
    "무궁화호": 3000,
}

seat_dict = {
    "입석": -2000,
    "좌석": 0
}

money = get_dest(input("춘천(운임 : 5000원) 부산(운임 :30000원) 대구(운임 20000원) 수원(운임 10000) 중 목적지를 한곳 입력하세요 : "))
money += get_class(input("KTX(10000원 추가) / 새마을호(5000원 추가) / 무궁화호(3000원 추가) 중 하나를 입력하세요 : "))
money += get_seat(input("좌석 / 입석(2000원 할인)중 하나를 입력하세요 : "))
print("지불하실 운임은 " + str(money) + "원 입니다.")
