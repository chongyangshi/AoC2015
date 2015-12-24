#Advent of Code December 24
#Written by icydoge - icydoge AT gmail dot com

from operator import mul
from itertools import combinations


def find_answer(content, section_weight):
    #Find the lowest subset with a sum equal to section_weight, and get QE.
    for i in range(1, len(content)):

        combs = combinations(content, i)
        solution_found = False

        for comb in combs:

            if sum(comb) == section_weight:
                QE = reduce(mul, comb)
                group_min = len(comb)
                solutions = [group_min, QE]
                solution_found = True
                break

        if solution_found:
            break

    return solutions


with open('inputs/gifts.txt') as f:
    content = map(int,f.read().splitlines())

#Part One
section_weight = sum(content) / 3
part_one_answer = find_answer(content, section_weight)[1]
print "QE for minimal Group 1 quantity (Part One):", part_one_answer

#Part Two
section_weight = sum(content) / 4
part_two_answer = find_answer(content, section_weight)[1]
print "QE for minimal Group 1 quantity with four sections (Part Two):", part_two_answer