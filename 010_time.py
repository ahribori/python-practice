import time

print(time.time())
print(time.ctime())
print(type(time.time()))
print(type(time.ctime()))

current_time = time.ctime()
print(current_time.split(' '))

for i in range(10):
    print(i)
    time.sleep(1)