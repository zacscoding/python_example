def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


'''
1. 리스트는 [과]으로 둘러싸지만, 튜플은 (과)으로 둘러 싼다.
2. 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 값을 바꿀 수 X
- 한개의 요소만을 가질 때 (1,)와 같이 ,를 반드시 붙여야 함
- t4 = 1,2,3 처럼 () 생략 가능
'''

t1 = ()
# ()
print(t1)
t2 = (1,)
# (1,)
print(t2)
t3 = (1, 2, 3)
# (1, 2, 3)
print(t3)
t4 = 1, 2, 3
# (1, 2, 3)
print(t4)
t5 = ('a', 'b', ('ab', 'cd'))
# ('a', 'b', ('ab', 'cd'))
print(t5)

# error
# t1 = (1, 2, 'a', 'b')
# del t1[0]
# t1[0] = 'c'

displayTitle("튜플의 인덱싱과 슬라이싱, 더하기(+), 곱하기(*)")

# 1. 인덱싱하기
t1 = (1, 2, 'a', 'b')
# 1
print(t1[0])
# b
print(t1[3])

# 2. 슬라이싱 하기
# (2, 'a', 'b')
print(t1[1:])

# 3. 튜플 더하기
t2 = (3, 4)
# (1, 2, 'a', 'b', 3, 4)
print(t1 + t2)

# 4. 튜플 곱하기
# (3, 4, 3, 4, 3, 4)
print(t2 * 3)