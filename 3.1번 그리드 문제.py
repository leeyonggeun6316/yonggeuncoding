changemoney = [500, 1000, 50]
count = 0
money = int(input("돈을 넣어 주십시요: "))
for change in changemoney:
    if money / change >0:
        count = money / change
        money = money % change
print(f"{count}개 입니다")
