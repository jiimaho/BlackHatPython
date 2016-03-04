import time
from pprint import pprint as pp


def call_n_times(times, func, *args):
    start = time.clock()
    pp("Starting loop")
    for i in range(1, times):
        func(*args)
    end = time.clock()
    pp("Elapsed time is {}".format(end - start))