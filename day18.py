#Advent of Code December 18
#Written by icydoge - icydoge AT gmail dot com

LIGHT_OFF = '.'
LIGHT_ON = '#'

def make_grid(lines):
    
    lights = []

    for line in lines:
        light_line = list(line)
        lights.append(light_line)

    return lights


def get_state(i, j, lights):

    #Coordinates beyond the edges are counted as off.
    if (i < 0) or (i > 99):
        return LIGHT_OFF

    if (j < 0) or (j > 99):
        return LIGHT_OFF

    return lights[j][i]


def operation(lights, part):

    new_arrangement = [[0 for x in range(100)] for x in range(100)]

    for i in range(0, len(lights)):
        for j in range(0, len(lights[i])):

            #For Part Two, the four corners are always on.
            if (part == 2) and (i in [0, 99]) and (j in [0, 99]):
                new_arrangement[i][j] = LIGHT_ON
                continue

            #Get the states of neighbours, including non-existent neighbouring coordinates beyond the edges.
            neighbours = []
            neighbours.append(get_state(i+1, j, lights))
            neighbours.append(get_state(i+1, j+1, lights))
            neighbours.append(get_state(i+1, j-1, lights))
            neighbours.append(get_state(i, j+1, lights))
            neighbours.append(get_state(i, j-1, lights))
            neighbours.append(get_state(i-1, j, lights))
            neighbours.append(get_state(i-1, j+1, lights))
            neighbours.append(get_state(i-1, j-1, lights))
            current_light = get_state(i, j, lights)

            #Set the new state of the light in new_arrangement.
            if current_light == LIGHT_ON:

                if (neighbours.count(LIGHT_ON) == 2) or (neighbours.count(LIGHT_ON) == 3):
                    new_arrangement[i][j] = LIGHT_ON

                else:
                    new_arrangement[i][j] = LIGHT_OFF

            else:

                if neighbours.count(LIGHT_ON) == 3:
                    new_arrangement[i][j] = LIGHT_ON

                else:
                    new_arrangement[i][j] = LIGHT_OFF

    return new_arrangement


with open('inputs/lights_2.txt') as f:
    content = f.read().splitlines()


#Part One
#Perform 100 steps of operations.
lights = make_grid(content)

for i in range(100):
    lights = operation(lights, 1)

part_one_answer = 0

for line in lights:
    for light in line:
        if light == LIGHT_ON:
            part_one_answer += 1

print "Number of lights on after 100 steps (Part One):", part_one_answer


#Part Two
lights = make_grid(content)

#Set the four corners to ON.
lights[0][0] = LIGHT_ON
lights[0][99] = LIGHT_ON
lights[99][0] = LIGHT_ON
lights[99][99] = LIGHT_ON

for i in range(100):
    lights = operation(lights, 2)
    
part_two_answer = 0

for line in lights:
    for light in line:
        if light == LIGHT_ON:
            part_two_answer += 1

print "Number of lights on after 100 steps, with 4 corners always on (Part Two):", part_two_answer
