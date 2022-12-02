from pathlib import Path

path = Path(__file__).parent / "../inputs/1-1.txt"

with path.open() as f:
    aoc_input = f.read().splitlines()

aoc_input = list(map(int, aoc_input))

results = []

for i,j in enumerate(aoc_input):
    if i == 0:
        pass
    else:
        if j > aoc_input[i-1]:
            results.append('i')
        else:
            results.append('d')

print(results.count('i'))