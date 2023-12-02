try:
    N = int(input(">> 출력할 라인 수는? : "))

    if N < 1 or N > 10:
        raise IndexError
    else:
        with open("baseball.txt", "r") as f:
            for _ in range(N):
                content = f.readline()
                print(content, end="")
except ValueError:
    print("입력은 정수로만 해주세요.")
except IndexError:
    print("입력 라인 수는 1~10까지 입니다.")
