cityList = []
while True:
    city = input("도시를 추가하세요 (종료 : exit) : ")
    if city == "exit":
        break
    else:
        cityList.append("'" + city[:3] + "'")
print("결과 >> " + ", ".join(cityList))