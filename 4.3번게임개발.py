# 세로 가로로
n,m = list(map(int,input().split()))
# 세로 가로 방향
x,y,direction = list(map(int,input().split()))
#지나간 곳을 파악하기 위한 맵 생성
datamap = [[0]*m for _ in range(n)]
# 방문 좌표 확인인
datamap[x][y] = 1
#전체 맵 입력
data = []
for _ in range(m):
    data.append(list(map(int,input().split())))
# 북동남서 반향 정의
dtype = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def turnreft():
    global direction
    direction = (direction - 1) % 4
#방문한 칸수수
count = 1
while True:
    # 4방향 모두 간 방향인지 확인
    checkd = False
    for _ in range(4):
        # 왼쪽으로 이동
        turnreft()
        tempx,tempy = dtype[direction]
        tempx += x 
        tempy += y  
        if 0<=tempx<=n and 0<=tempy<=m and data[tempx][tempy] == 0 and datamap[tempx][tempy] == 0:
            x,y = tempx,tempy
            datamap[x][y] = 1
            count +=1
            checkd = True
    # 양면이 다 가본곳이지 확인
    if checkd == False:
        tempx,tempy = dtype[(direction + 2) % 4]
        tempx += x 
        tempy += y  
        if 0<=tempx<=n and 0<=tempy<=m and data[tempx][tempy] == 0:
            x,y = tempx,tempy
        else:
            break
print(count)