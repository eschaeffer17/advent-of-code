Day = '3-1'

from pathlib import Path
import string

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read().splitlines()

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority = [x+1 for x in list(range(52))]

points = dict(zip(letters, priority))
results = []

for i in aoc_input:
    comp1 = set([*i[:int(len(i)/2)]])
    comp2 = set([*i[int(len(i)/2):]])
    results.append(points[list(comp1.intersection(comp2))[0]])

print(sum(results))