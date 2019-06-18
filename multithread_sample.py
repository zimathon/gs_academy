import os
import threading

MAX_COUNT = 100000000
ITERATION = 50000000

def whoami(what):
    count = 0
    for n in range(MAX_COUNT):
        if count % ITERATION ==0:
            print("{} Process {} thread= {} count {}".format(what,os.getpid(),threading.current_thread(),count))
        count +=1
    print("end {} Thread {}".format(what,threading.current_thread()))

for n in range(10):
    p = threading.Thread(target=whoami,args=("Thread {}".format(n),))
    p.start()