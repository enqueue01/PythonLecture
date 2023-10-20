N = int(input())
if (N < 2 or N > 9):
    print("error")
    exit(0)
for i in range(1, 10):
    print(f"{N} * {i} = {N * i}")
