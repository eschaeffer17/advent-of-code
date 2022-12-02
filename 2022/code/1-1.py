Day = '1-1'

from pathlib import Path

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read()

results = []

for i in aoc_input.split('\n\n'):
    results.append(list(map(int, list(filter(None, i.split('\n'))))))

answer = max([sum(x) for x in results])