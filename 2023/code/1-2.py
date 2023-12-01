Day = '1'

from pathlib import Path
import re

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read()

results = []

word_map = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}


for i in aoc_input.split('\n'):
    if len(i)>0:
        tup_list = []

        for index, char in enumerate(i):
            if char.isdigit():
                tup_list.append((index, char))
        for key in word_map:
            if i.find(key)>=0:
                tup_list.append((i.find(key), word_map[key]))
            if i.rfind(key)>=0:
                tup_list.append((i.rfind(key), word_map[key]))
        decoded = sorted(tup_list)
        print(decoded)
        print(decoded[0][1] + decoded[-1][1])

        results.append(int(decoded[0][1] + decoded[-1][1]))


print(sum(results))