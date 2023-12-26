import numpy as np

print(f"추출된 번호: {sorted(np.random.choice(range(1, 46), size=6, replace=False))}")

# while True:
#     num = np.random.randint(1, 45, size=6)
#     if len(set(num)) == 6:
#         print(sorted(num))
#         break
