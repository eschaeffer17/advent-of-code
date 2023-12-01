Day = '13-1'

from common import read_daily_input
from itertools import zip_longest
import numpy as np

aoc_input = read_daily_input(Day)

pkts = [[[2]],[[6]]]+[eval(x) for x in aoc_input]

def compare(l, r) -> bool:

    for ll, rr in zip_longest(l, r, fillvalue=None):
        if ll == None: return True
        if rr == None: return False
        
        if isinstance(ll, int) and isinstance(rr, int):
            if ll > rr: return False
            if ll < rr: return True
        else:
            if isinstance(rr, int): rr = [rr]
            if isinstance(ll, int): ll = [ll]
            
            ret = compare(ll, rr)
            if ret in [True, False]: return ret


while True: 
    for i in range(len(pkts)-1):
        if compare(pkts[i], pkts[i+1]) == False:
            pkts[i], pkts[i+1] = pkts[i+1], pkts[i]
            done = False

    if done == True: break
    done = True

print((pkts.index([[2]]) + 1) * (pkts.index([[6]]) + 1))