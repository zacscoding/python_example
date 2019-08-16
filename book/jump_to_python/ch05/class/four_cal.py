class FourCal:

    def setdata(self, first, second):
        self.second = second
        self.first = first

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first % self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
