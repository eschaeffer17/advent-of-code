Day = '6-2'

from common import read_daily_input

aoc_input = read_daily_input(Day)

packet_strs = []

for i in aoc_input:
    for j in range(0,len(i)-13):
        packet = i[j:j+14]
        if len(set(packet))==14:
            packet_strs.append(j)

print(min(packet_strs)+14)