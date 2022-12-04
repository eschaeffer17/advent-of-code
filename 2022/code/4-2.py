Day = '4-2'

from pathlib import Path

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read().splitlines()

result = []
for i in aoc_input:
    j = i.split(',')
    rng1 = j[0].split('-')
    rng1 = range(int(rng1[0]),int(rng1[1])+1)

    rng2 = j[1].split('-')
    rng2 = range(int(rng2[0]),int(rng2[1])+1)

    same_ids = range(max(rng1[0], rng2[0]), min(rng1[-1], rng2[-1])+1)
    
    full_overlap = (rng1 == same_ids or rng2 == same_ids)
    any_overlap = len(same_ids)>0

    result.append(any_overlap)

answer = result.count(True)
print(answer)