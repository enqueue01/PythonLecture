class Circle:
    PI = 3.14

    def __init__(self, radius=0):
        self.radius = radius

    def calcPerimeter(self):
        return print(f"원의 둘레 : {self.radius * 2 * self.PI:.1f}")

    def calcArea(self):
        return print(f"원의 면적 : {self.radius * self.radius * self.PI}")


if __name__ == "__main__":
    x = Circle(5)
    x.calcPerimeter()
    x.calcArea()
