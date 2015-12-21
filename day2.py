#Advent of Code December 2
#Written by icydoge - icydoge AT gmail dot com

with open('inputs/paper.txt') as f:
    content = f.read().splitlines()[:-1] #Remove last empty line

part_one_answer = 0
part_two_answer = 0

for box in content:
    dimensions = sorted(map(int,box.split('x')))
    slack = dimensions[0] * dimensions[1]
    wrapping = 2 * (dimensions[0] * dimensions[1] + dimensions[1] * dimensions[2] + dimensions[0] * dimensions[2])
    ribbon = (dimensions[0] + dimensions[1]) * 2
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    part_one_answer += wrapping + slack
    part_two_answer += ribbon + bow

print "Total square feet of wrapping paper (Part One):", part_one_answer
print "Total feet of ribbon (Part Two):", part_two_answer