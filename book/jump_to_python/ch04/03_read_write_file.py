def displayTitle(title):
    separator = "=" * 50
    print(separator + "  " + title + "  " + separator)


displayTitle("파일 생성하기")
"""
open(파일이름, 파일 열기 모드)
r : 읽기 모드
w : 쓰기 모드
a : 추가 모드 (마지막에 새로운 내용 추가)

"""
# write & read file

filepath = "D:\\python\\test.txt"

f = open(filepath, "w")
for i in range(1, 11):
    data = "%d line... \n" % i
    f.write(data)
f.close()
print("success to write file")

displayTitle("how to read 1)")
print("start to read file")
f = open(filepath, "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

displayTitle("how to read 2)")
f = open(filepath, "r")
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()

displayTitle("파일에 새로운 내용 추가하기")
f = open(filepath, "a")
for i in range(11, 20):
    data = "%d line...\n" % i
    f.write(data)
f.close()

displayTitle("how to read 3)")
f = open(filepath, "r")
# 파일 내용 전체를 문자열로 리턴
data = f.read()
print(data)
f.close()

displayTitle("with문과 함께 사용하기")

with open(filepath, "r") as f:
    print(f.read())
