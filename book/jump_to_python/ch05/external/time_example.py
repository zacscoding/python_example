import time

print("time.time() : ", time.time())
print("time.localtime(time.time()) : ", time.localtime(time.time()))
print("time.asctime(time.localtime(time.time())) : ", time.asctime(time.localtime(time.time())))
print("time.ctime() : ", time.ctime())
print("time.strftime('%x', time.localtime(time.time())) : ", time.strftime("%x", time.localtime(time.time())))

for i in range(3):
    print(i)
    time.sleep(1)
