#Advent of Code December 1
#Written by C Shi - icydoge AT gmail dot com

with open('inputs/floor.txt') as f:
    content = f.read()

floors = list(content)

#Part One
current_floor = 0

for f in floors:

    if f == '(':
        current_floor += 1

    elif f == ')':
        current_floor -= 1

    else:
        raise ValueError("Unacceptable direction.")

part_one_answer = current_floor
print "Santa is at this floor (Part One):", part_one_answer

#Part Two
current_floor = 0
position = 0
part_two_answer = None

for f in floors:

    position += 1

    if f == '(':
        current_floor += 1

    elif f == ')':
        current_floor -= 1

        if current_floor < 0:
            part_two_answer = position
            break

    else:
        raise ValueError("Unacceptable direction.")

if part_two_answer != None:
    print "Santa enters basement at this position (Part Two):", part_two_answer
else:
    print "Error in Part Two, Santa never enters the basement."