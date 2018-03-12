def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


odd = [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9]
print(odd)

a = [1, 2, ['Life', 'is']]
# [1, 2, ['Life', 'is']]
print(a)

displayTitle("리스트의 인덱싱과 슬라이싱")

# 리스트의 인덱싱
a = [1, 2, 3]
# 1
print(a[0])
# 3
print(a[2])
# 3 (마지막 요소)
print(a[-1])
# 4
print(a[0] + a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
# 1
print(a[0])
# ['a', 'b', 'c']
print(a[-1])
# ['a', 'b', 'c']
print(a[3])
# a
print(a[-1][0])

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
# [1, 2] 0<=index<2
print(a[0:2])
# [1, 2]
print(a[:2])
# [3, 4, 5]
print(a[2:])

# 중첩된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# [3, ['a', 'b', 'c'], 4]
print(a[2:5])
# ['a', 'b']
print(a[3][:2])

displayTitle("리스트 연산자")

# 리스트 더하기 (+)
a = [1, 2, 3]
b = [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
print(a + b)

# 리스트 반복하기 (*)
a = [1, 2, 3]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(a * 3)

displayTitle("리스트의 수정, 변경, 삭제")

# 리스트에서 하나의 값 수정하기
a = [1, 2, 3]
a[2] = 4
# [1, 2, 4]
print(a)

# 리스트에서 연속된 범위의 값 수정하기
# [1, 2, 4]
print(a)
# [2]
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
# [1, 'a', 'b', 'c', 4]
print(a)
a = [1, 2, 4]
# [1, ['a', 'b', 'c'], 4] a[x:y]와 a[x]는 전혀 다름
a[1] = ['a', 'b', 'c']
print(a)

# [] 를 사용해 리스트 요소 삭제하기
a = [1, 'a', 'b', 'c', 4]
# [1, 'a', 'b', 'c', 4]
print(a)
a[1:3] = []
# [1, 'c', 4]
print(a)

# del 함수를 사용해 리스트 요소 삭제하기
# [1, 'c', 4]
print(a)
del a[1]  # a[1]인 'c' 삭제
# [1, 4]
print(a)
del a[0:2]
# []
print(a)

displayTitle("리스트 관련 함수들")
# 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
# [1, 2, 3, 4]
print(a)
[1, 2, 3, 4, [5, 6]]
a.append([5, 6])
print(a)

# 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a.sort()
# [1, 2, 3, 4]
print(a)
a = ['a', 'c', 'b', 'A', 'C', 'B']
a.sort()
# ['A', 'B', 'C', 'a', 'b', 'c']
print(a)

# 리스트 뒤집기 (reverse)
a = ['a', 'b', 'c', 'c']
a.reverse()
# ['c', 'c', 'b', 'a']
print(a)

# 위치 반환(index)

a = [1, 2, 3]
# 2
print(a.index(3))
# 0
print(a.index(1))
# error
# print(a.index(0))

# 리스트에 요소 삽입 (insert(a,b)) : a번째에 b 삽입
a = [1, 2, 3]
a.insert(0, 4)  # a[0] 위치에 4 삽입
# [4, 1, 2, 3]
print(a)
a.insert(3, 5)
# [4, 1, 2, 5, 3]
print(a)

# 리스트 요소 제거 (remove) : 첫 번째 나오는 요소 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
# [1, 2, 1, 2, 3]
print(a)
a.remove(3)
# [1, 2, 1, 2]
print(a)

# 리스트 요소 끄집어 내기(pop) : 맨 마지막 요소를 반환 & 그 요소 삭제
a = [1, 2, 3, 4]
# 4
print(a.pop())
# [1, 2, 3]
print(a)
# 2
print(a.pop(1))
# [1, 3]
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
# 2
print(a.count(1))

# 리스트 확장 (extend(x)) : 원래의 리스트 a에 x리스트를 더하게 된다.
a = [1, 2, 3]
a.extend([4, 5])
# [1, 2, 3, 4, 5]
print(a)
b = [6, 7]
a.extend(b)
# [1, 2, 3, 4, 5, 6, 7]
print(a)