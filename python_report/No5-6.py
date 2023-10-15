dic = {
    'kim': 12000,
    'lee': 11000,
    'han': 3000,
    'choi': 5000,
    'hwang': 18000
}

for id, mile in dic.items():
    print(f"아이템: {id}, 마일리지: {mile}")

print() # No6

max_id = max(dic, key=dic.get)
print(f"{max_id} 님이 {dic[max_id]} 으로 가장 높은 점수입니다.")

# key_max = max(dic.keys(), key=(lambda k: dic[k]))
# value_max = dic[key_max]
# print(f"{key_max} 님이 {value_max} 으로 가장 높은 점수입니다.")