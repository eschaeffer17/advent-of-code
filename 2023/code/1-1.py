Day = '1'

from pathlib import Path
import re

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read()

results = []

for i in aoc_input.split('\n'):
    if len(i)>0: 
        results.append(int(re.findall(r'\d',i)[0] + re.findall(r'\d',i)[-1]))

print(sum(results))