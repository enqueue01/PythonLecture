max, min = 91, 79
for i in range(13):
    print(" " * i, end=" ")
    for j in range(65 + i, max):
        print(chr(j), end="")
    max -= 1
    print()

for i in range(13):
    print(" " * (12 - i), end=" ")
    for j in range(77 - i, min):
        print(chr(j), end="")
    min += 1
    print()
