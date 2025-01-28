N,M,K =0,0,0
N, M, K = list(map(int, input().split()))
data = []
data = (list(map(int, input().split())))
data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수 사용 횟수 계산
count_first = (M // (K + 1)) * K + (M % (K + 1))

# 결과 계산
result = count_first * first + (M - count_first) * second

print(f"결과: {result}")