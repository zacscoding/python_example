def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


def displaySubject(title):
    separator = "-" * 10
    print(separator + "  " + title + "  " + separator)


"""
집합 자료형의 특징
1. 중복을 허용X
2. 순서가 없음(Unordered)
"""

displayTitle("집합 자료형 특징")
s1 = set([1, 2, 3])
# {1, 2, 3}
print(s1)
# [1, 2, 3]
print(list(s1))
# (1, 2, 3)
print(tuple(s1))
s2 = set("Hello")
# {'H', 'e', 'o', 'l'}
print(s2)

displayTitle("집합 자료형 활용")
displaySubject("교집합, 합집합, 차집합")

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1. 교집합 ( &, intersection() )
# {4, 5, 6}
print(s1 & s2)
# {4, 5, 6}
print(s1.intersection(s2))

# 2. 합집합 ( | , union() )
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))

# 3. 차집합 ( - , difference() )
# {1, 2, 3}
print(s1 - s2)
# {1, 2, 3}
print(s1.difference(s2))

displayTitle("집합 자료형 관련 함수들")

# 값 1개 추가하기 (add)

s1 = set([1, 2, 3])
s1.add(4)
# {1, 2, 3, 4}
print(s1)

# 값 여러 개 추가(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6, 'a'])
# {1, 2, 3, 4, 5, 6, 'a'}
print(s1)

# 특정 값 제거(remove)
s1 = set([1, 2, 3])
s1.remove(1)
# {2, 3}
print(s1)
