import numpy as np

ary = np.random.randint(1, 100, size=(10, 10))
print("생성된 10x10 Array:\n" + "array([" + "," "\n\t".join([f"{row}" for row in ary]) + "])")

print("\n2, 3 Columm Indexing:\n" + "array([" + "," "\n\t".join([f"{row[1:3]}" for row in ary]) + "])")
