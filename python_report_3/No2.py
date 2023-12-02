class Calculator:
    def __init__(self, *args):
        self.nums = args

    def sum(self):
        return sum(self.nums)

    def avg(self):
        return sum(self.nums) / len(self.nums)


if __name__ == "__main__":
    cal_1 = Calculator(1, 2, 3, 4, 5)
    print(cal_1.sum())
    print(cal_1.avg())
    cal_2 = Calculator(4, 5, 6)
    print(cal_2.sum())
    print(cal_2.avg())