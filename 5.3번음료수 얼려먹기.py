# 거의 답안지 배낌 
# 다시 풀어야 함함

# 가로(width) 세로(length)
width,length = map(int,input().split())
grapth = []
for i in range(length):
    grapth.append(list(map(int,input().split()))[:width])

# 주변 노드 방문하기
def dfs(x,y):
    # 범위를 벗어 나면 취소
    if x < 0 or x >= length or y < 0 or y >= width:
        return False
    if grapth[x][y] == 1: 
        return False
    else:
        # 방문 했으니 문 닫기
        grapth[x][y] = 1
        # 네 방향으로 이동동
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True

count = 0
for i in range(length): 
    for j in range(width): 
        if dfs(i,j):
            count+=1
print(count)