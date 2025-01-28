n = int(input())
data = {}  

for _ in range(n):
    name, grade = input().split()
    data[name] = int(grade)  

sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)

for name, _ in sorted_data:
    print(name)