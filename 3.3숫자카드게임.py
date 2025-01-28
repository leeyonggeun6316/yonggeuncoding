n,m = list(map(int,input().split()))
result = 0  
for _ in range(n):
    # m개만 읽고 나머지는 버려짐짐
    data = list(map(int, input().split()))[:m]
    temp = min(data)
    if temp>result:
        result = temp
print(result)