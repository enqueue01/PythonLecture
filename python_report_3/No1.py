class Human:
    def __init__(self, name="", age=0, gender=""):
        self.name = name
        self.age = age
        self.gender = gender

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"{self.name}, {self.age}, {self.gender}")


if __name__ == "__main__":
    kim = Human("김하성", 27, "남")
    jang = Human("장원영", 18, "여")
    unknown = Human("모름", 0, "모름")
    unknown.setInfo("산타할아버지", 100, "남")
    kim.printInfo()
    jang.printInfo()
    unknown.printInfo()
