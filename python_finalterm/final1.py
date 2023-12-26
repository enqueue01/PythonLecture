import random

# 로또 번호 생성
winNum = set()
while len(winNum) != 7:
    winNum.add(random.randint(1, 45))

winNum = list(winNum)
bonusNum = winNum.pop(-1)  # 보너스 번호 pop
winNum.sort()

print("당첨 번호입니다 :", *winNum)
print("보너스 번호 입니다 :", bonusNum)

# 파일에서 사용자 로또 번호 로딩
with open("lottery_number.txt", "r") as f:
    lines = f.readlines()

# 각 회차별 당첨 확인
print("당첨 내역입니다.")
for cnt, line in enumerate(lines):
    userNum = list(map(int, line.split(" ")))
    matchCount = len(set(winNum) & set(userNum))
    bonusMatch = bonusNum in userNum
    notify = ""
    if matchCount == 3:
        notify = "5 등"
    elif matchCount == 4:
        notify = "4 등"
    elif matchCount == 5 and not bonusMatch:
        notify = "3 등"
    elif matchCount == 5 and bonusMatch:
        notify = "2 등"
    elif matchCount == 6:
        notify = "1 등"
    else:
        notify = "당첨되지 않았습니다."
    print(f"{cnt + 1} 회차 : {notify}")
