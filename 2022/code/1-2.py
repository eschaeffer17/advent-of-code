Day = '1-2'

from pathlib import Path

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read()

lst = []

for i in aoc_input.split('\n\n'):
    lst.append(list(map(int, list(filter(None, i.split('\n'))))))

results = [sum(x) for x in lst]
results.sort()

answer = sum(results[-3:])