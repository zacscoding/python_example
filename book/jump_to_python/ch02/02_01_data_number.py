"""
정수, 실수, 복소수, 8진수, 16진수
"""

# === 정수
print("=== Integer ===")
a = 123
print(a)

# === 실수
print("=== real === ")
a = 1.2
print(a)
# 42400000000.0
a = 4.24E10
print(a)
# 0.0424
a = 4.24e-2
print(a)

# === 8진수
print("=== Octal ===")
a = 0o177
# 127
print(a)

# === 16진수
print("Hexadecimal")
a = 0x8ff
# 2303
print(a)

# === 복소수
print("Complex")
a = 1 + 2j
b = 3 - 4J
# (4-2j)
print(a + b)
# 1.0
print(a.real)
# 2.0
print(a.imag)
# (1-2j)
print(a.conjugate())
# 2.23606797749979 == root(1^2 + 2^2)
print(abs(a))

# ** 연산자
print("** operator")
a = 3
b = 4
# 81 == 3^4
print(a ** b)

# % 연산
print("% operator")
a = 10
b = 3
# 1
print(a % 3)

# // 연산 (소수점 버림)
print("// operator")
a = 7
b = 4
# 1
print(a // b)
