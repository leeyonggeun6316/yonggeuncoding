n = int(input())
array = [0]*1000
array[0] = 1
array[1] = 3
for i in range(2,n):
    array[i] = (array[i-1]+array[i-2]*2)%796796
print(array[i-1])

