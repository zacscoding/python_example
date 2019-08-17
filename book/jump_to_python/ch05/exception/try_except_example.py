try:
    print(4 / 0)
except:
    print("Exception occur..")

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

try:
    f = open("foo.txt", "r")
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
finally:
    print("finally is called..")

try:
    f = open("foo.txt", "r")
except FileNotFoundError as e:
    pass


class Bird:
    def fly(self):
        raise NotImplementedError("must implement fly methods")


class Eagle(Bird):
    pass


try:
    eagle = Eagle()
    eagle.fly()
except NotImplementedError as e:
    print("Raised exception", e)

print("End..")
