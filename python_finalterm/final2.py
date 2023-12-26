with open("word.txt", "r", encoding="utf-8") as f:
    words = f.readlines()
    N = len(words)
    for i in range(N):
        for j in range(0, N - i - 1):
            if len(words[j]) > len(words[j + 1]):
                temp = words[j]
                words[j] = words[j + 1]
                words[j + 1] = temp

            elif len(words[j]) == len(words[j + 1]):
                if words[j] > words[j + 1]:
                    temp = words[j]
                    words[j] = words[j + 1]
                    words[j + 1] = temp

with open("sortedWord.txt", "w", encoding="utf-8") as f:
    f.writelines(words)
