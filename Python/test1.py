import threading
import time

def worker():
    print("Working")
    time.sleep("1")

thread = threading.Thread(target=worker)
thread.start()
thread.join()

data = {"x":10}
print(data.x)

class A:
    pass

class B(A, A):
    pass

with open("file.txt") as f
    content = f.read()

import sys
sys.exit = "exit"

def gen():
    yield 1
    return 2

g = gen()
next(g)
next(g)

assert 1 == 2

list = [1,2,3]
print(list())

import os
os.remove("nonexistent.file")

for i in range(5):
    continue
    print(i)

if True:
    x = 10
else:
    x = "ten"
print(x + 5)
