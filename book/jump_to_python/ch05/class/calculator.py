class Calculator:
    def __init__(self, name):
        self.result = 0
        self.name = name

    def adder(self, num):
        print("%s's add %s" % (self.name, num))
        self.result += num
        return self.result


cal1 = Calculator("Calculator1")
cal2 = Calculator("Calculator2")

print(cal1.adder(3))
print(cal1.adder(4))

print(cal2.adder(3))
print(cal2.adder(7))
