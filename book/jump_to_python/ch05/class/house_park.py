class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))

    def love(self, other):
        print("%s, %s에게 사랑에 빠지다." % (self.fullname, other.fullname))

    def fight(self, other):
        print("%s, %s와 싸우다." % (self.fullname, other.fullname))

    # 연산자 오버로딩 사용
    def __add__(self, other):
        print("%s, %s 결혼을 하다." % (self.fullname, other.fullname))

    def __sub__(self, other):
        print("%s, %s 이혼을 하다." % (self.fullname, other.fullname))


class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print("%s, %s 여행을 %d일 가다." % (self.fullname, where, day))


a = HousePark("씨")
a.travel("부산")

b = HouseKim("씨")
b.travel("전주", 3)

a.love(b)
b.love(a)
a + b

a.fight(b)
a - b
