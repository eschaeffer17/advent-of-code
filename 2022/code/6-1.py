Day = '6-1'

from common import read_daily_input

aoc_input = read_daily_input(Day)

packet_strs = []

for i in aoc_input:
    for j in range(0,len(i)-3):
        packet = i[j:j+4]
        if len(set(packet))==4:
            packet_strs.append(j)

print(min(packet_strs)+4)