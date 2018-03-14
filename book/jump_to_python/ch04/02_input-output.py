def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


displayTitle("사용자 입력")
# a = input()
# print("입력 값 : %d" % int(a))

"""
입력 : asdfasdf
입력 값 : asdfasdf
"""
# a = input("입력 : ")
# print("입력 값 : " + a)

displayTitle("print() 함수")
"""
lifeistoo short
lifeistoo short
"""
print("life" "is" "too short")
print("life" + "is" + "too short")

# 문자열 띄여쓰기는 , 로 구분
# life is too short
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')
