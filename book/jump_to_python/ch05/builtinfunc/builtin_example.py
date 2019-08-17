# abs : 절대값
print("abs(3) : ", abs(3))
print("abs(-3) : ", abs(-3))

# all : 모두 true 인지
print("all([1, 2, 3]) : ", all([1, 2, 3]))
print("all([1, 2, 0]) : ", all([1, 2, 0]))

# any : 하나라도 true 인지
print("any([1, 0, 0]) : ", any([1, 0, 0]))
print("any([0, \"\"]) : ", any([0, ""]))

# chr : 아스키코드 -> 해당 문자
print("chr(97) : ", chr(97))
print("chr(48) : ", chr(48))


# dir : 객체가 자체적으로 가지고 있는 변수나 함수
class Sample:
    local_variable = 3

    def sayName(self):
        print("my name is ...")


print(dir([1, 2, 3]))
print(dir({'1': 'a'}))
print(dir(Sample()))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'local_variable', 'sayName']
"""

# divmod : a를 b로 나눈 몫 + 나머지 튜플 반환
(q, r) = divmod(7, 3)
print(q, r)

# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체 반환
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval : 실행 가능한 문자열(1+2, 'hi'+'a')을 입력 받아 문자열을 실행한 결과값 리턴
print("eval(1 + 2) : ", eval('1 + 2'))
print("eval(\"'hi' + 'va'\") : ", eval("'hi' + 'va'"))
print("eval('divmod(4,3)') : ", eval('divmod(4,3)'))


# filter : 첫번째 인수 == 함수 , 두번째 인수 == 반복 가능한 자료형
def positive(x):
    return x > 0


print("list(filter(positive, [1, -3, 2, 0, -5, 6])) : ", list(filter(positive, [1, -3, 2, 0, -5, 6])))
print("list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])) : ", list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex : 정수 -> 16 진수
print("hex(234) : ", hex(234))
print("hex(3) : ", hex(3))

# id : 고유 주소값(레퍼런스) 반환
a = 3
print("id(3) : ", id(3))
print("id(a) : ", id(a))
b = a
print("id(b) : ", id(b))
b = 5
print("id(b) : ", id(b))

# input : 사용자 입력을 받는 함수
# print("input() >>")
# a = input()
# print("a : ", a)

# int 정수형으로 변환
print("int(3) : ", int(3))
print("int(3.4) : ", int(3.4))
print("int('3') : ", int('3'))
# 2진수로 표현 된 '11' > 10진수 변환
print("int('1011',2) : ", int('1011', 2))


# isinstance : 인스턴스가 그 클래스의 인스턴스인지 체크
class Person:
    pass


a = Person()
print("isinstance(a, Person) : ", a, Person())
a = 3
print("isinstance(a, Person) : ", isinstance(a, Person))

# lambda
sum = lambda a, b: a + b
print("sum(3, 4) : ", sum(3, 4))

myList = [lambda a, b: a + b, lambda a, b: a * b]
print("myList[0](3, 4) : ", myList[0](3, 4))
print("myList[1](3, 4) : ", myList[1](3, 4))

# len 입력값의 길이 리턴
print("len('aaa') : ", len('aaa'))
print("len([1, 2, 3]) : ", len([1, 2, 3]))

# list : 반복 가능한 자료형 s를 입력받아 리스트로 만들어주는함수
print("list('python') : ", list("python"))


# map(f, iterable) 함수와 반복 가능한 자료형을 입력받아 함수가 적용 된 결과 리턴
def two_times(x): return x * 2


print("list(map(two_times, [1, 2, 3, 4])) : ", list(map(two_times, [1, 2, 3, 4])))

# max : 반복 가능한 자료형 입력 후 최대값 리턴
print("max([1,2,3]) : ", max([1, 2, 3]))

# min : 반복 가능한 자료형 입력 후 최소값 리턴
print("min([1, 2, 3]) : ", min([1, 2, 3]))

# oct : 정수 형태 -> 8진수
print("oct(9)", oct(9))

# open : 파일 읽기 (w : 쓰기, r : 읽기, a : 추가, b : 바이너리 모드)
f = open("sample.txt", 'r')
data = f.read()
print("f.read() : ", data)
f.close()

# ord : 문자의 아스키 코드값  리턴
print("ord('a') : ", ord('a'))

# pow : x의 y제곱 한 결과
print("pow(2, 3) : ", pow(2, 3))

# range : range([start,] stop [,step])
print("list(range(5)) : ", list(range(5)))
print("list(range(5, 10)) : ", list(range(5, 10)))
print("list(range(1, 10, 2)) : ", list(range(1, 10, 2)))

# sorted 입력 값 정렬
print("sorted([3, 1, 2]) : ", sorted([3, 1, 2]))
a = [3, 1, 2]
result = a.sort()
print(result)
print("after sorted a : ", a)

# str : 문자열 형태로 객체 변환
print("str(3) : ", str(3))
print("str('hi') : ", str('hi'))
print("str('hi'.upper()) : ", str('hi'.upper()))

# tuple : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴
print("tuple('abc') : ", tuple('abc'))
print("tuple([1, 2, 3]) : ", tuple([1, 2, 3]))
print("tuple((1, 2, 3)) : ", tuple((1, 2, 3)))

# type : 자료형 반환
print("type('abc') : ", type('abc'))
print("type('[]') : ", type([]))

# zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할
print("list(zip([1, 2, 3], [4, 5, 6])) : ", list(zip([1, 2, 3], [4, 5, 6])))
print("list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) : ", list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print("list(zip('abc', 'def')) : ", list(zip("abc", "def")))
