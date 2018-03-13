def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


displayTitle("for문의 기본 구조")
test_list = ['one', 'two', 'three']
"""
one
two
three
"""
for i in test_list:
    print(i)

displayTitle("다양한 for문의 사용")
"""
3
7
11
"""
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

displayTitle("for문의 응용")

marks = [90, 25, 67, 45, 80]
number = 0
print(marks)
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격" % number)
    else:
        print("%d번 학생은 불합격" % number)

displayTitle("for문과 continue")
marks = [90, 25, 67, 45, 80]
number = 0
print(marks)
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생은 합격" % number)

displayTitle("for문과 함꼐 자주사용하는 range 함수")
a = range(10)
# range(0, 10) first <= index < second
print(a)

sum = 0
for i in range(1, 11):
    sum = sum + i
# range(1,11)의 합 : 55
print("range(1,11)의 합 : %d" % sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번쨰 학생은 합격" % (number + 1))

displayTitle("리스트 안에 for문 포함하기")
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
# [3, 6, 9, 12]
print(result)

# 리스트 내포(List comprehension)을 사용
#
"""
1. [표현식 for 항목 in 반복 가능 객체 if 조건]
2. [표현식 for 항목1 in 반복 가능 객체1 if 조건1
           for 항목2 in 반복 가능 객체2 if 조건2
           ...
           for 항목n in 반복 가능 객체n if 조건n
    ]
"""

result = [num * 3 for num in a]
# [3, 6, 9, 12]
print(result)

# 3을 곱한 수 중 짝수만?
result = [num * 3 for num in a if num % 2 == 0]
# [6, 12]
print(result)

# 구구단 + 리스트 내포

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
print(result)
