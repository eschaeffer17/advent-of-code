Day = '3-2'

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

for i in range(0,len(aoc_input),3):
    comp1 = set([*aoc_input[i]])
    comp2 = set([*aoc_input[i+1]])
    comp3 = set([*aoc_input[i+2]])
    results.append(points[list(comp1.intersection(comp2).intersection(comp3))[0]])

answer = sum(results)