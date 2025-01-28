from collections import deque
#  세로(length) 가로(width)
length,width = map(int,input().split())

# 가로(width) 세로(length)
graph = []
for i in range(length):
    graph.append(list(map(int, input().strip())))
    

# 반향 정의 위 아래 오른쪽 왼쪽
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            tempx = x + dx[i]
            tempy = y + dy[i]

            # 범위 안에 있을 시
            if 0 <= tempx < length and 0 <= tempy < width:
                # 괴물이 아닌 경우
                if graph[tempx][tempy] == 1:
                    graph[tempx][tempy] = graph[x][y]+1
                    queue.append((tempx, tempy))
    print(graph[length-1][width-1])

bfs(0,0)
'''시뮬레이션
5 7 
1011011
1000101
1111111
0000101
1111101
'''