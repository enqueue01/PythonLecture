import numpy as np

ary = np.random.randint(1, 100, size=(10, 10))
print("생성된 10x10 Array:\n" + "array([" + "," "\n\t".join([f"{row}" for row in ary]) + "])")
print(f"최대값:{np.max(ary)}")
print(f"최소값:{np.min(ary)}")
