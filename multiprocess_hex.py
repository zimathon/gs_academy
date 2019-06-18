
import os
import multiprocessing
import threading
import hashlib
import datetime

MAX_COUNT = 10000000

def tomd5(what):
    for n in range(MAX_COUNT):
        hexstring = hashlib.md5(n.to_bytes(16,'big')).hexdigest()
    print("end {} Process {}".format(what,os.getpid()))
    print(datetime.datetime.now())

print(datetime.datetime.now())
for n in range(10):
    p = multiprocessing.Process(target=tomd5, args=("Process {}".format(n),))
    # p = threading.Thread(target=tomd5,args=("Thread {}".format(n),))
    p.start()
