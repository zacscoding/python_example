def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


"""
문자열
    "python"    : 참
    ""          : 거짓
리스트
    [1,2,3]     : 참
    []          : 거짓
튜플
    ()          : 거짓
딕셔너리
    {}          : 거짓
숫자형
    0이 아닌 숫자 : 참
    0           : 거짓
기타
    None        : 거짓
"""

#
a = [1, 2, 3, 4]
count = 0
while a:  # a 가 참인 동안
    a.pop()
    count += 1
# 4
print(count)

# False
if []:
    print("True")
else:
    print("False")

# True
if [1, 2, 3]:
    print("True")
else:
    print("False")
