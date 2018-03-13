def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


money = 1
if money:
    print("true")
# print("error") << error 들여쓰기
else:
    print("false")

displayTitle("비교연산자")
# <,<=, >, >= , == , !=

displayTitle("and or not")
# x or y , x and y, not x
# True
print(not 0)

displayTitle("x in s, x not in s")
# True
print(1 in [1, 2, 3])
# True
print(4 not in [1, 2, 3])
# True
print('test' in ['test', 'test3'])

displayTitle("조건문 pass")
if 1:
    pass
else:
    print("else")

displayTitle("다양한 조건을 판단하는 elif")
pocket = ['paper', 'cellphone']
# elif is true
if 'money' in pocket:
    print("money in pocket")
elif 1:
    print("elif is true")
elif 'paper' in pocket:
    print("paper in pocket")

