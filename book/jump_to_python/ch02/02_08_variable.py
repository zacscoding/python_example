import sys


def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


"""
파이썬에서 3은 상수가 아닌 정수형 객체
"""

# <class 'int'>
print(type(3))

# 43
print(sys.getrefcount(3))
a = 3
b = 3
# True
print(a is b)
# 45
print(sys.getrefcount(3))

displayTitle("변수를 만드는 여러가지 방법")
a, b = ('python', 'life')
# python
print(a)
# life
print(b)
(a, b) = 'python', 'life'
# python
print(a)
# life
print(b)

# 리스트로 변수를 만들기
[a, b] = ['python', 'life']
# python
print(a)
# life
print(b)

# 변수에 같은 값 대입
a = b = 'python'
# python python
print(a + ' ' + b)

# 변수 바꾸기
a = 3
b = 5
a, b = b, a
# 5
print(a)
# 3
print(b)

displayTitle("메모리에 생성된 변수 없애기")
a = 3
b = 3
# 51
print(sys.getrefcount(3))
del (a)
# 50
print(sys.getrefcount(3))
del (b)
# 49
print(sys.getrefcount(3))
# error undefined
# print(a)

displayTitle("리스트를 변수에 넣고 복사")
a = [1, 2, 3]
b = a
a[1] = 4
# [1, 4, 3]
print(a)
# [1, 4, 3]
print(b)

# [:]를 이용한 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
# [1, 4, 3]
print(a)
# [1, 2, 3]
print(b)

# copy 모듈 이용
from copy import copy

a = [1, 2, 3]
b = copy(a)
a[1] = 4
# [1, 4, 3]
print(a)
# [1, 2, 3]
print(b)
# False
print(b is a)
