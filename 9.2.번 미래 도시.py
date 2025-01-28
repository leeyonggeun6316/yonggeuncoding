# 무한
INF = int(1e9)
# n 회사 수,m 경로의 개수
n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신은 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

# 간선은 1로
for _ in range(m):
    i,j = map(int,input().split())
    graph[i][j] = 1
    graph[j][i] = 1

# 거쳐야 할 곳 x,최종 목적지 k
x,k = map(int,input().split())

# 방문한 회사
visited = [False]*(n+1)
# 최단 거리 테이블
distance = [INF] * (n+1)

# 경우지 i 출발 점 j 도착 점 l
for i in range(1,n+1):
    for j in range(1,n+1):
            for l in range(1,n+1):
                graph[j][l] = min(graph[j][l],graph[j][i]+graph[i][l])

if graph[1][k]+graph[k][x] >= INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])