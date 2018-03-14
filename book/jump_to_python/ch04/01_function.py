def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


def sum(a, b):
    return a + b


a = 1
b = 2
c = sum(a, b)
print(c)


def say():
    print("Zacscoding")


say()
# error
# say(a)

displayTitle("여러 개의 입력값을 받는 함수")


def sum_many(*args):
    print("sum_many() is called")
    print(args)
    sum = 0
    for i in args:
        sum = sum + i
    return sum


"""
sum_many() is called
(1, 2, 3, 4, 5)
15
"""
sum = sum_many(1, 2, 3, 4, 5)
print(sum)


# error
# print(sum_many([1, 2, 3, 4, 5]))
# print(sum_many((1, 2, 3, 4, 5)))


def calculate(type, *args):
    print("calculate is called")
    print(args)
    if type == "sum":
        result = 0
        for i in args:
            result = result + i
        return result
    elif type == "mul":
        result = 1
        for i in args:
            result = result * i
        return result
    else:
        return 0


"""
calculate is called
(1, 2, 3)
6
calculate is called
(1, 2, 3)
6
"""
print(calculate("sum", 1, 2, 3))
print(calculate("mul", 1, 2, 3))

displayTitle("함수의 결과값은 하나")


def sum_and_mul(a, b):
    return a + b, a * b


# (6, 8) 튜플을 반환
tupleResult = sum_and_mul(2, 4)
print(tupleResult)

# sum : 6, mul : 8
sum, mul = sum_and_mul(2, 4)
print("sum : {0}, mul : {1}".format(sum, mul))

displayTitle("입력 인수에 초기값 설정")


def say_myself(name, age, man=True):
    print("이름 : {0}, 나이 : {1} , 성별(남?) : {2}".format(name, age, man))


# 이름 : zac, 나이 : 10 , 성별(남?) : True
say_myself("zac", 10)
# 이름 : zac, 나이 : 10 , 성별(남?) : False
say_myself("zac", 10, False)

displayTitle("변수 범위")

variable = 1


def vartest(variable):
    variable = variable + 1


vartest(variable)
# 1
print(variable)

displayTitle("함수안에서 밖에 변수 변경하기")
global_variable = 1


def vartest():
    global global_variable
    global_variable = global_variable + 1


"""
before vartest () : 1
after vartest () : 2
"""
print("before vartest () : %d" % global_variable)
vartest()
print("after vartest () : %d" % global_variable)
