class InvalidNumberException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}는 3의 배수가 아닙니다 InvalidNumberException을 발생시킵니다."


def three_multi(N):
    if N != 0 and N % 3 == 0:
        print(f"{N}은 3의 배수가 맞습니다!")
    else:
        raise InvalidNumberException(N)


if __name__ == "__main__":
    try:
        three_multi(int(input("3의 배수를 입력하세요 : ")))
    except InvalidNumberException as e:
        print(e)
