n,k = map(int,input().split())
arraya = list(map(int,input().split()[:n]))
arrayb = list(map(int,input().split()[:n]))
arraya.sort()
arrayb.sort(reverse=True)
for i in range(k):
    if arraya[i]<arrayb[i]:
        arraya[i],arrayb[i] = arrayb[i],arraya[i]
    else:
        break
print(sum(arraya))
