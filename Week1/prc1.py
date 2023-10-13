# s = 'CoupangAuction'
# print(s[7:],s[:7])


# print("안녕하세요?")
# print("제 이름은 xxx 입니다.")
# name = input("당신 이름은 무엇인가요?")
# print("안녕하세요!",name+"님 만나서 반가워요")


# print("안녕하세요? 저는 더하기를 잘 하지요.")
# while True:
#     try:
#         num = int(input("정수 입력: "))
#         print("result : ", num + 5)
#         break
#     except ValueError as e:
#         print("숫자 입력 해주세요.", e)
#         continue
#     except (SyntaxError, EnvironmentError):
#         print("문법 오류!")
#         continue

# num1 = int(input("첫번째 정수를 입력해 주세요."))
# num2 = int(input("두번째 정수를 입력해 주세요."))
# print(str(num1), "과 " + str(num2), "을 더한 값은", num1 + num2, "입니다.")


# a = 10
# b = 15
# a,b = b,a

# print(f"{1+2}, {3+5}")
# print("{}, {}".format(1+2, 3+5))
# a = 1+5
# print("hi:", a)
# print("{:9d}".format(52)) # 5d 10
# print("{:9d}".format(252)) # 5d 10
# print("{:9d}".format(3252)) # 5d 10
# print("{:9d}".format(2)) # 5d 10
# print("{:9d}".format(-252)) # 5d 10
# print("{:9d}".format(2322135)) # 5d 10
# print(type(int("{:15.0f}".format(3.141592))))
# print("{:15.0f}".format(3.141592)) # 5d 10
# print("{:03d}".format(152)) # 5d 10
# print("00010") # 05d 10
# print(f"{a} \"hi\" + {a} = {a+5}")
# print(a + "'""hi""' '+ '" + a + "'='" + a+5)
# a = "hi"
# 'h' in a

# from datetime import datetime
#
# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# a = 4
#
# if a > 5:
#     print("크다")
# else:
#     print("작다")
# elif a < 3:
#     print("3보단 작다")
# else:
#     pass
# x = 15
# if 10 < x < 20:
#     print(x)

# tti = ["원숭이", "닭","개","돼지","쥐","소","범","토끼","용","뱀","말","양"]
#
# a = int(input("연도 : "))
# print(tti[a % 12])


# a = [1,2,3]
#
# index = 0
# for i in enumerate(a): # 0 ~ 2
#     print(index, i)

#     index += 1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output = [[], [], []]
#
# for index, number in enumerate(numbers):
#     print(index, number)
# output[number%3 - 1].append(number)
# number 1 = index 0
# 2 = 1
# 3 = 2
# 4 = 0
# 5 = 1
# 6 = 2
# 7 = 0
# 8 = 1
# 9 = 2

# [ 1 4 7 ] [ 2 5 8 ] [ 3 6 9 ]
# 0 1 2
#
# dict_a = {
#     "name": ["아이언맨","히어로"],
#     "type": "히어로"
# }
# a, b = dict_a["name"]
# print(a, b)
# print(dict_a["name"][0],dict_a["name"][1])

dict_a = {}
dict_a["name"] = "구름"
del dict_a["name"]
print(dict_a)

pets = [
    {"name": "구름", "age": 5},
    {"name": "하늘", "age": 3},
    {"name": "초코", "age": 1}
]
print(type(pets))
for pet in pets:
    print(type(pet))
    name, age = pet.values()
    print(name, age)
