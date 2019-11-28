from multiprocessing import Process,Queue,Pipe
from slave import serialize
import time


def timer(*args, f=None):
    before = time.time()
    f(*args)
    after = time.time()
    return after - before



big_str = ' '.join(['abcdeftghijklmnopq\n' for y in range(1000000)]) + ' '
print(len(big_str))

parent_conn,child_conn = Pipe()
p = Process(target=serialize, args=(child_conn,big_str))

def run(proc, conn):
    proc.start()
    conn.recv()


print(timer(p, parent_conn, f=run))
