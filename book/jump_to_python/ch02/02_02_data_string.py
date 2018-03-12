"""
문자열 자료형
"""
lineSeparator = "=" * 50

# == 문자열 생성
str1 = "Hello World"
str2 = 'Python is fun'
str3 = """Life is too short, You need python"""
str4 = '''zaccoding'''

print(str1)
print(str2)
print(str3)
print(str4)

# == 문자열에 ' 포함

food = "Python's favorite food is perl"
# Python's favorite food is perl
print(food)

say = '"Python is very easy." he says'
# "Python is very easy." he says
print(say)

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"
print(food)
print(say)

# new line
multiline = "Life is too short\nYou need python"
print(multiline)
print("--")

multiline = '''Life is too short
You need python
'''
print(multiline)
print("--")

multiline = """Life is too short
You need python"""
print(multiline)
print("--")

# == 문자열 연산
print("================= 문자열 연산 =================")
print("1. 더해서 연결")
head = "Python"
tail = " is fun"
# Python is fun
print(head + tail)

print("2. 문자열 곱하기")
a = "python"
# pythonpython
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# == 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
# e
print(a[3])
# n
print(a[-1])
# True
print(a[0] == a[-0])
# Life 0 <= i < 4
print(a[0:4])
# You need Python , 19 <= i <length-1
print(a[19:])
# Life is too short, 0 <= i <19
print(a[:19])

a = "Pithon"
# Python
print(a[:1] + 'y' + a[2:])

# == 문자열 포매팅
"""
%s : 문자열 // %c : 문자1개 // %d : 정수 // %f 부동 소수
%o : 8진수 // %x : 16진수 // %% : Literal % (문자 '%' 자체)
"""
print("=" * 50)
# I eat 3 apples
print("I eat %d apples" % 3)
# I eat five apples
print("I eat %s apples" % "five")

number = 3
# I eat 3 apples
print("I eat %d apples" % number)

day = "three"
# I ate 3 apples. so I was sick for three days
print("I ate %d apples. so I was sick for %s days" % (number, day))

# I have 3 apples
print("I have %s apples" % 3)
# Error is 98%
print("Error is %d%%" % 98)

# == 포맷 코드와 숫자 함께 사용하기

# 1. 정렬과 공백
#         hi (전체 length 10중 0:7 공백, 8,9 'h', 'i'
print("%10s" % "hi")
# hi        jane
print("%-10sjane" % "hi")

print(lineSeparator)
print("2. 소수점 표현")
# 3.1416
print("%0.4f" % 3.141592)
#     3.1416 (전체 길이 10 중 소수점4개 표현, 공백 4개)
print("%10.4f" % 3.141592)

print(lineSeparator + " 문자열 관련 함수 " + lineSeparator)
a = "hobby"
# 2
print(a.count('b'))

# 위치알려주기1 (find)
a = "Python is best choice"
# 10
print(a.find('b'))
# -1
print(a.find('k'))

# 위치 알려주기2 (index)
a = "Life is too short"
# 8
print(a.index('t'))
# error
# Traceback (most recent call last):
# print(a.index('k'))
# ValueError: substring not found
# print(a.index('k'))

# 문자열 삽입 (join)
a = ","
# a,b,c,d
print(a.join("abcd"))

# upper
a = 'hi'
# HI
print(a.upper())
# hi
print(a.upper().lower())

# 왼쪽 공백 지우기 (lstrip)
a = " hi"
print(a.lstrip())

# 오른쪽 공백 지우기 (rstrip)
a = "hi "
print(a.rstrip())

# 양쪽 공백 지우기
a = " hi "
print(a.strip())

# 문자열 바꾸기 (replace)
a = "Life is too short"
# Your leg is too short
print(a.replace("Life", "Your leg"))

# 문자열 나누기 (split)
a = "Life is too short"
# 공백을 기준으로 문자열 나눔
# ['Life', 'is', 'too', 'short']
print(a.split())
a = "a:b:c:d"
# ['a', 'b', 'c', 'd']
print(a.split(':'))

# 고급 문자열 포매팅
print(lineSeparator + " 고급 문자열 포매팅 " + lineSeparator)
# I eat 3 apples
print("I eat {0} apples".format(3))
# I eat five apples
print("I eat {0} apples".format("five"))
number = 3
# I eat 3 apples
print("I eat {0} apples".format(number))

number = 10
day = "three"
# I ate 10 apples. so I was sick for three days.
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
# I ate three apples. so I was sick for 10 days.
print("I ate {1} apples. so I was sick for {0} days.".format(number, day))

# 이름으로 넣기
# I ate 10 apples. so I was sick for 3 days.
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

# 인덱스와 혼용해서 넣기
# I ate 10 apples. so I was sick for 3 days.
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# 왼쪽 정렬
# hi        k
print("{0:<10}".format("hi") + "k")

# 오른쪽 정렬
#         hik
print("{0:>10}".format("hi") + "k")

# 가운데 정렬
#     hi    k
print("{0:^10}".format("hi") + "k")

# 공백 채우기
# ====hi====k
print("{0:=^10}".format("hi") + "k")
# hi!!!!!!!!k
print("{0:!<10}".format("hi") + "k")

# 소수점 표현하기
y = 3.42134234
# 3.4213
print("{0:0.4f}".format(y))
#     3.4213
print("{0:10.4f}".format(y))

# '{' or '}' 문자 표현하기
# { and }
print("{{ and }}".format())