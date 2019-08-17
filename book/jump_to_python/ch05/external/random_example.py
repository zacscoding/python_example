import random

print("random.random() : ", random.random())
print("random.randint(1, 10) : ", random.randint(1, 10))


def random_pop(data):
    idx = random.randint(0, len(data) - 1)
    return data.pop(idx)


data = [1, 2, 3]
while data:
    print(random_pop(data))

data = [1, 2, 3, 4, 5]
random.shuffle(data)
print("After shuffle : ", data)
