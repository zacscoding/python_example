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
print(a*2)

print("="*50)
print("My Program")
print("="*50)

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
print("I ate %d apples. so I was sick for %s days" %(number, day))

# I have 3 apples
print("I have %s apples" % 3)
# Error is 98%
print("Error is %d%%" % 98)












