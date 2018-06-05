import time
from multiprocessing import Pool


def f(x):
    time.sleep(0.1 - x/100)
    print(x * x)

with Pool(10) as p:
    p.map(f, range(10))
