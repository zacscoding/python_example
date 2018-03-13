def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


"""
나무를 1 찍음
나무를 2 찍음
나무를 3 찍음
나무를 4 찍음
나무를 5 찍음
나무가 넘어감
while문 밖
"""

treeHit = 0
while treeHit < 5:
    treeHit = treeHit + 1
    print("나무를 %d 찍음" % treeHit)
    if treeHit == 5:
        print("나무가 넘어감")

print("while문 밖")

displayTitle("while문 직접 만들기")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

# number = 0
# while number != 4:
#    print(prompt)
#    number = int(input())
#    print("Your choice is %d" % number)

displayTitle("while문 강제로 빠져나가기")

coffee = 5
money = 300
while money:
    coffee = coffee - 1
    print("커피 1개 판매. 남은 coffee %d개" % coffee)
    if not coffee:
        print("coffee : 0 개이므로 종료")
        break

displayTitle("조건에 맞지 않는 경우 맨 처음으로 돌아가기")

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

displayTitle("무한루프")
#while True:
#    print("Press Ctrl+C")

