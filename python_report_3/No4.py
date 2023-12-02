class Grade:
    subject = {"kor": "국어", "eng": "영어", "math": "수학"}

    def __init__(self, name="", kor=0, eng=0, math=0):
        self.name = name
        self.scores = {"kor": kor, "eng": eng, "math": math}

    def average(self):
        return print(f"{self.name}의 평균점수는 {sum(self.scores.values()) / len(self.scores)}점 입니다.")

    def score(self, course):
        return print(f"{self.name}의 {self.subject[course]} 점수는 {self.subject[course]}점 입니다.")

    def __del__(self):
        print(f"{self.name} 학생 객체는 삭제되었습니다.")


if __name__ == "__main__":
    p1 = Grade("Kim", 60, 80, 65)
    p2 = Grade("Park", 80, 49, 93)
    p1.score("kor")
    p2.score("eng")
    p2.average()
    del(p2)
    #input()
