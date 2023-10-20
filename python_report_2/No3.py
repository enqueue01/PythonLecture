import random

random_num = set()
while True:
    random_num = {random.randrange(1, 46) for _ in range(6)}
    if len(random_num) == 6:
        print(sorted(random_num))
        break

# pythonic
print(sorted(random.sample(range(1, 46), 6)))
