import random

N = random.randrange(1, 100)
num = 0
while N != num:
    num = int(input("숫자를 예측해보세요 (1~100) >> "))
    print("숫자가 작습니다" if N > num else "정답입니다." if N == num else "숫자가 높습니다.")