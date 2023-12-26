def finder(file, word):
    with open(file, "r") as f:
        num = f.read().count(word)
        print(f'"{file}" 파일 안에는 총 {num}번의 {word}가 있습니다.')

if __name__ == "__main__":
    finder("yesterday.txt", "yesterday")
