n = int(input()) 
data = input().split()  
x, y = 1, 1  

for i in data:
    if i == 'R':
        if x + 1 <= n:  
            x += 1
    elif i == 'L':
        if x - 1 >= 1: 
            x -= 1
    elif i == 'U':
        if y - 1 >= 1:  
            y -= 1
    elif i == 'D':
        if y + 1 <= n:  
            y += 1

print(x, y)  