import threading
import time


def say(message):
    while True:
        time.sleep(1)
        print(message)


for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(10):
    time.sleep(0.5)
    print(i)
