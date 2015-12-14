#Advent of Code December 13
#Written by icydoge - icydoge AT gmail dot com
#I changed from a TSP(Day9)-adapted solution to brute force due to debugging an unrelated isssue, therefore brute force searching is used for this solution. The same algorithm in Day 9 can be applied here with minimum adaptation.

import itertools

def get_happiness(lose_gain, happiness_units):

    if lose_gain == "lose":
        return -1 * int(happiness_units)
    elif lose_gain == "gain":
        return int(happiness_units)
    else:
        raise ValueError("Unexpected input for happiness unit value.")

def get_plan_happiness(happiness_map, seating_plan):

    happiness = 0

    for i in range(0,len(seating_plan)-1):
        happiness += int(happiness_map[seating_plan[i]][seating_plan[i+1]]) + int(happiness_map[seating_plan[i+1]][seating_plan[i]])

    #Two people ended up seating next to each other at the end.
    happiness += int(happiness_map[seating_plan[0]][seating_plan[-1]]) + int(happiness_map[seating_plan[-1]][seating_plan[0]])

    return happiness


with open('table.txt') as f:
    content = f.read().splitlines()

#Part One
#Construct the table
happiness = {}
for statement in content:
    line = statement[:-1].split(' ')
    #Build 2-D dictionary (happiness table)
    if line[0] in happiness:
        happiness[line[0]][line[10]] = get_happiness(line[2], line[3])
    else:
        happiness[line[0]] = {}
        happiness[line[0]][line[10]] = get_happiness(line[2], line[3])

people = happiness.keys()

#Start from the first permutation
people_permutations = [list(i) for i in list(itertools.permutations(people))]
best_plan = people_permutations[0]
best_happiness = get_plan_happiness(happiness, people_permutations[0])

#Iterate through every possible permutation to find the plan with most happiness change
for i in range(1,len(people_permutations)):
    if get_plan_happiness(happiness, people_permutations[i]) > best_happiness:
        best_plan = people_permutations[i]
        best_happiness = get_plan_happiness(happiness, people_permutations[i])

part_one_answer = best_happiness
print "Maximum happiness change (Part One) is:", part_one_answer

#Part Two
#Add 'You' to the happiness table with value 0 to everyone.
happiness['You'] = {}
for person in people:
    happiness[person]['You'] = 0
    happiness['You'][person] = 0

people.append('You')

#Start from the first permutation
people_permutations = [list(i) for i in list(itertools.permutations(people))]
best_plan = people_permutations[0]
best_happiness = get_plan_happiness(happiness, people_permutations[0])

#Iterate through every possible permutation to find the plan with most happiness change
for i in range(1,len(people_permutations)):
    if get_plan_happiness(happiness, people_permutations[i]) > best_happiness:
        best_plan = people_permutations[i]
        best_happiness = get_plan_happiness(happiness, people_permutations[i])

part_two_answer = best_happiness
print "Maximum happiness change with 'You' (Part Two) is:", part_two_answer



