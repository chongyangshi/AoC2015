#Advent of Code December 16
#Written by icydoge - icydoge AT gmail dot com

with open('aunt_matching.txt') as fi:
    content = fi.read().splitlines()

properties = {}
for item in content:

    line = item.split(' ')
    properties[line[0][:-1]] = int(line[1])

with open('aunts.txt') as f:
    content = f.read().splitlines()


#Part One
for item in content:

    line = item.split(' ')

    if (properties[line[2][:-1]] == int(line[3][:-1])) and (properties[line[4][:-1]] == int(line[5][:-1])) and (properties[line[6][:-1]] == int(line[7])):
        part_one_answer = int(line[1][:-1])
        break

print "The Aunt giving the gift (Part One) is Sue", part_one_answer


#Part Two
for item in content:

    line = item.split(' ')

    aunt_properties = {}
    aunt_properties[line[2][:-1]] = int(line[3][:-1]) 
    aunt_properties[line[4][:-1]] = int(line[5][:-1])
    aunt_properties[line[6][:-1]] = int(line[7])

    is_that_aunt = True

    for key in aunt_properties:

        if key == "cats" or key == "trees":
            if properties[key] >= aunt_properties[key]:
                is_that_aunt = False

        elif key == "pomeranians" or key == "goldfish":
            if properties[key] <= aunt_properties[key]:
                is_that_aunt = False

        elif properties[key] != aunt_properties[key]:
            is_that_aunt = False

    if is_that_aunt:
        part_two_answer = line[1][:-1]
        break

print "The real Aunt giving the gift (Part Two) is Sue", part_two_answer