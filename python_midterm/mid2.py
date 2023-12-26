block_num = int(input())
block_crdnt = []

for _ in range(block_num):
    block_crdnt.append(list(map(int, input().split(" "))))
    if (not 0 <= block_crdnt[-1][0] < 5) or (not 0 <= block_crdnt[-1][1] < 5):
        print("block_crdnt is out of range(5X5) program exit...")
        exit(0)

person_crdnt = [list((map(int, input().split(" "))))]
if (not 0 == person_crdnt[-1][0]) or (not 0 <= block_crdnt[-1][1] < 5):
    print("person_crdnt is out of range(5X5) program exit...")
    exit(0)

move_list = input().split(" ")
if len(move_list) != 5:
    print("move limit is 5! program exit...")
    exit(0)

for move in move_list:
    if move not in ["R", "L"]:
        print("move is NOT R or L program exit...")
        exit(0)
    match move:
        case "R":
            if person_crdnt[0][1] < 5:
                person_crdnt[0][1] += 1
        case "L":
            if person_crdnt[0][1] > 0:
                person_crdnt[0][1] -= 1
    for i in range(block_num):
        block_crdnt[i][0] -= 1
        if block_crdnt[i] == person_crdnt[0]:
            print("hit")
            exit(0)

print("no hit")