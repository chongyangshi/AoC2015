#Advent of Code December 6
#Written by C Shi - icydoge AT gmail dot com
#Dumb and ugly code, be aware

with open('inputs/lights.txt') as f:
    content = f.read().splitlines()[:-1]

lights = [[0 for i in range(1000)] for i in range(1000)]

for line in content:

    line_split = line.split(' ')

    if line_split[0] == "toggle":

        lower_indices = line_split[1].split(',')
        higher_indices = line_split[3].split(',')

        for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
            for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                if lights[i][j] == 1:
                    lights[i][j] = 0
                else:
                    lights[i][j] = 1

    elif line_split[0] == "turn":

        lower_indices = line_split[2].split(',')
        higher_indices = line_split[4].split(',')

        if line_split[1] == "on":

            for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
                for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                    lights[i][j] = 1

        elif line_split[1] == "off":

            for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
                for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                    lights[i][j] = 0

        else:
            raise ValueError("Not turning on or turning off!")

    else:
        raise ValueError("Unexpected action!")

part_one_answer = sum(row.count(1) for row in lights)
print "Lights lit after operations (Part One): ", part_one_answer

lights = [[0 for i in range(1000)] for i in range(1000)]

for line in content:

    line_split = line.split(' ')

    if line_split[0] == "toggle":

        lower_indices = line_split[1].split(',')
        higher_indices = line_split[3].split(',')

        for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
            for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                lights[i][j] += 2

    elif line_split[0] == "turn":

        lower_indices = line_split[2].split(',')
        higher_indices = line_split[4].split(',')

        if line_split[1] == "on":

            for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
                for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                    lights[i][j] += 1

        elif line_split[1] == "off":

            for i in range(int(lower_indices[0]),int(higher_indices[0])+1):
                for j in range(int(lower_indices[1]),int(higher_indices[1])+1):
                    if lights[i][j] > 0:
                        lights[i][j] -= 1

        else:
            raise ValueError("Not turning on or turning off!")

    else:
        raise ValueError("Unexpected action!")

part_two_answer = 0
for i in lights:
    for j in i:
        part_two_answer += j
print "Total brightness after operations (Part Two): ", part_two_answer
