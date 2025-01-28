n = input()
strtype = ['a','b','c','d','d','g','h']
width = 1
for i in range(7):
    if strtype[i] == n[0]:
        width +=i
        break
steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
count = 0
height = int(n[1])
for x,y in steps:
    if 1<=(width + x)<=8 and 1<=(height + y)<=8:
        count +=1
print(count)

