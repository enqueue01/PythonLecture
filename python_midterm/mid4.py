mark = [["", "", ""], ["", "", ""], ["", "", ""]]
Player = "O"
Computer = "X"


def draw_board():  # 판
    print("     1     2     3 \n  ┌─────┬─────┬─────┐")
    print(f"1 │  {mark[0][0]:<3}│  {mark[0][1]:<3}│  {mark[0][2]:<3}│")
    print("  ├─────┼─────┼─────┤")
    print(f"2 │  {mark[1][0]:<3}│  {mark[1][1]:<3}│  {mark[1][2]:<3}│")
    print("  ├─────┼─────┼─────┤")
    print(f"3 │  {mark[2][0]:<3}│  {mark[2][1]:<3}│  {mark[2][2]:<3}│")
    print("  └─────┴─────┴─────┘")


def game_checker(check, x, y):  # 최대 중첩 차수 2차
    if mark[y].count(check) == 3:  # 행검사
        return True
    if (mark[0][x] + mark[1][x] + mark[2][x]).count(check) == 3:  # 열검사
        return True
    if x == y and (mark[0][0] + mark[1][1] + mark[2][2]).count(check) == 3:  # 좌에서 우 대각선 검사
        return True
    if x + y == 2 and (mark[0][2] + mark[1][1] + mark[2][0]).count(check) == 3:  # 우에서 좌 대각선 검사
        return True


def game_checker_com(check, x, y):  # 최대 중첩 차수 1차
    if mark[y].count(check) == 3:  # 행검사
        return True
    if (mark[0][x] + mark[1][x] + mark[2][x]).count(check) == 3:  # 열검사
        return True
    if (mark[0][0] + mark[1][1] + mark[2][2]).count(check) == 3:  # 좌에서 우 대각선 검사
        return True
    if (mark[0][2] + mark[1][1] + mark[2][0]).count(check) == 3:  # 우에서 좌 대각선 검사
        return True


def center_control():  # 최대 중첩 차수 1차
    if mark[1][1] == "":
        return 1, 1


def corner_control():  # 최대 중첩 차수 1차
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]  # 모서리

    if mark[0][0] == "":
        return corners[0]  # (0, 0)
    if mark[0][2] == "":
        return corners[1]
    if mark[2][0] == "":
        return corners[2]
    if mark[2][2] == "":
        return corners[3]  # (2, 2)


def defense(target):  # 최대 중첩 차수 2차
    target_locate = False
    check = False
    for i in range(3):
        if mark[i][0] == "":  # 빈칸이면
            mark[i][0] = target  # target 넣고
            check = True  # check 토글
        if game_checker_com(target, 0, i):  # 넣었을 때 승리 조건 검사
            mark[i][0] = ""  # 조건이 있다면 빈칸으로 다시 보정
            return i, 0
        if check:  # 조건이 없을 때 토글된 check를 이용
            mark[i][0] = ""  # 조건이 없어도 빈칸으로 다시 보정
            check = False  # check를 False로 토글

        if mark[i][1] == "":
            mark[i][1] = target
            check = True
        if game_checker_com(target, 1, i):
            mark[i][1] = ""
            return i, 1
        if check:
            mark[i][1] = ""
            check = False

        if mark[i][2] == "":
            mark[i][2] = target
            check = True
        if game_checker_com(target, 2, i):
            mark[i][2] = ""
            return i, 2
        if check:
            mark[i][2] = ""
            check = False

    return target_locate


def not_lose():  # 최대 중첩 차수 1차 (빈칸 생성 3차 제외)
    center = center_control()
    if center:  # 중앙이 비어있다면 중앙
        return center

    result = defense(Computer)  # 컴퓨터가 이기는 경우
    if result:
        return result

    block_move = defense(Player)  # 플레이어가 이기는 경우
    if block_move:
        return block_move

    corner = corner_control()  # 코너가 비어 있으면 코너
    if corner:
        return corner

    empty_spaces = []  # 비어있는 곳 찾기
    for y in range(3):
        for x in range(3):
            if mark[y][x] == "":
                empty_spaces.append((y, x))
    if empty_spaces:
        return empty_spaces[0], empty_spaces[1]
    else:
        return False  # 빈칸이 없으므로(무승부)


def loop():
    try:
        x, y = [int(num) - 1 for num in input("놓을 곳의 좌표를 입력하세요 : ").split(",")]
        if x not in range(3) or y not in range(3) or not mark[y][x] == "":
            print("이미 입력된 좌표 또는 범위를 초과하였습니다. 프로그램을 종료합니다... ")
            exit(0)
        mark[y][x] = Player
    except Exception:
        print("올바른 형식의 좌표를 입력하세요. 프로그램을 종료합니다...")
        exit(0)
    draw_board()

    if game_checker(Player, x, y):
        print("플레이어 승리")
        exit(0)

    move = not_lose()
    if move != False:
        print("컴퓨터가 놓을 차례입니다.")
        mark[move[0]][move[1]] = Computer
        draw_board()

        if game_checker_com(Computer, move[1], move[0]):
            print("안타깝습니다... 컴퓨터의 승리입니다.")
            exit(0)
    else:
        print("무승부입니다.")
        exit(0)


# __main__
draw_board()
loop()
loop()
loop()
loop()
loop()
