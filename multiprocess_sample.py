import os
import multiprocessing

MAX_COUNT = 100000000
ITERATION = 50000000

def whoami(what):
    count = 0
    for n in range(MAX_COUNT):
        if count % ITERATION == 0:
            print("{} Process {} count {}".format(what,os.getpid(),count))
        count +=1
    print("end {} Process {}".format(what,os.getpid()))

for n in range(10):
    p = multiprocessing.Process(target=whoami,args=("Process {}".format(n),))
    p.start()