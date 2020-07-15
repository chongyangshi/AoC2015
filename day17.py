#Advent of Code December 17
#Written by C Shi - icydoge AT gmail dot com

from itertools import combinations

with open('inputs/containers.txt') as f:
    content = sorted(map(int,f.read().splitlines()))

min_comb = 150 / max(content)  #At least this many containers needed achieve 150.

count = 0 #Number of ways to pack.
packing = {}  
#Dictionary with keys as number of containers sum to 150, 
#values as number of ways with that many containers.

for i in range(min_comb, len(content)):

    combs = combinations(content, i) #All possible combinations with i many of containers.

    for way in combs:

        if sum(way) == 150:
            count += 1

            if len(way) in packing:
                packing[len(way)] += 1
            else:
                packing[len(way)] = 1

part_one_answer = count
part_two_answer = packing[min(packing)]

print "Number of possible ways to pack 150 litres (Part One):", part_one_answer
print "Number of possible ways to pack 150 litres with minimum number of containers (Part Two):", part_two_answer