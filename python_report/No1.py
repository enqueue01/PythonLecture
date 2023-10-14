N = int(input())
for _ in range(N):
    word_list = []
    for word in input():
        if word in word_list and word != word_list[-1]:
            N -= 1
            break
        else:
            word_list.append(word)
print(N)

#pythonic.ver
# n = int(input())
# count = 0
#
# for _ in range(n):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         count += 1
# print(count)