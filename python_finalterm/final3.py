INF = 999
dis = [INF] * 6
path = [0] * 6
visit = [False] * 6
matrix = [[0, 2, 5, 1, INF, INF],
          [INF, 0, 3, 2, INF, INF],
          [INF, 3, 0, INF, INF, 5],
          [INF, INF, 3, 0, 1, INF],
          [INF, INF, 1, INF, 0, 2],
          [INF, INF, INF, INF, INF, 0]]


def Dijkstra(start):
    dis[start] = 0
    path[start] = start

    for _ in range(6):
        min_value = INF
        x = -1

        for i in range(6):
            if not visit[i] and dis[i] < min_value:
                min_value = dis[i]
                x = i
        if x == -1:
            break

        visit[x] = True

        for i in range(6):
            cost = matrix[x][i]
            if cost != INF:
                newd = dis[x] + cost
                if newd < dis[i]:
                    dis[i] = newd
                    path[i] = x

    return dis, path


if __name__ == '__main__':
    try:
        start = int(input("출발노드: ")) - 1
        if start < 0 or start > 5:
            print("1~6 사이 수를 입력해주세요! 종료합니다...")
            exit(0)

        end = int(input("도착노드: ")) - 1
        if end < 0 or end > 5:
            print("1~6 사이 수를 입력해주세요! 종료합니다...")
            exit(0)

        dis, path = Dijkstra(start)

        if dis[end] == INF:
            print("경로가 없습니다!")
        else:
            print(f"{start + 1}에서 {end + 1}까지의 최소 경로는: ", end="")
            temp = end
            s = str(end + 1)
            while temp != start:
                s = str(path[temp] + 1) + " -> " + s
                temp = path[temp]
            print(s)
            print(f"{start + 1}에서 {end + 1}까지의 Cost는: {dis[end]}")

    except Exception:
        print("1~6사이의 정수를 입력을 해주세요! 종료합니다...")
        exit(0)
