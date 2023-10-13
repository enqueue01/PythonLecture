dic = {'커피음료': 7, '펜': 3, '종이컵': 2, '우유': 1, '콜라': 4, '책': 5}
while True:
    try:
        name = input("please input name")
        if name in dic:
            print(dic[name])
        elif name == "end":
            break
        else:
            print("취급하지 않는 물건입니다")
    except:
        break