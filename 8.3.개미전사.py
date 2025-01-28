n = int(input())
array = list(map(int,input().split()))
a = [0]*100
a[0] = array[0]
a[1] = max(a[0],array[1])
for i in range(2,n):
    a[i] = max(a[i-1],a[i-2]+array[i])
print(a[n-1])