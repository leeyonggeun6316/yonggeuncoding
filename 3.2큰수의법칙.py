N,M,K =0,0,0
while True:
    N, M, K = list(map(int, input().split()))
    if not (2 <= N <= 1000 and 1 <= M <= 10000 and 1 <= K <= 10000):
        # 조건이 맞지 않음음
        print("입력 값이 범위를 벗어났습니다. 다시 입력해 주세요.")
    else:
        break  # 조건이 맞음 종료료
data = []
while True:
    temp = (list(map(int, input().split())))

    if len(temp) == N:
        # N개의 데이터 입력 확인인
        for i in temp:
            # 범위 검사
            valid = True    
            if not 1<=i<=10000:
                print("1이상 10000이하의 숫자만 입력해주십시요.")
                valid = False
        if valid:
            data = temp
            break
data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수 사용 횟수 계산
count_first = (M // (K + 1)) * K + (M % (K + 1))

# 결과 계산
result = count_first * first + (M - count_first) * second

print(f"결과: {result}")