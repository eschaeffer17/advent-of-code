Day = '13-1'

from common import read_daily_input
from itertools import zip_longest
import numpy as np

aoc_input = read_daily_input(Day, '\n\n')

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

n = 1
outcome_lst = []
for i in aoc_input:
    left = eval(i.split('\n')[0])
    right = eval(i.split('\n')[1])
    outcome_lst.append([n,compare(left,right)])
    n+=1

print(sum([x[0] for x in outcome_lst if x[1]==True]))