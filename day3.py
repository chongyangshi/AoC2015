#Advent of Code December 3
#Written by icydoge - icydoge AT gmail dot com

with open('directions.txt') as f:
    content = f.read()[:-1] #remove new line character at the end

route = list(content)

#Part One
moves = [(0,0)]
current_x = 0
current_y = 0

#Santa moves then deliver a present
for i in route:

    if i == "^":
        current_y += 1

    elif i == "v":
        current_y -= 1

    elif i == ">":
        current_x += 1

    elif i == "<":
        current_x -= 1

    else:
        raise ValueError("Unacceptable direction.")

    moves += [(current_x, current_y)]

part_one_answer = len(set(moves))
print "Number of houses with at lest one present (Part One):", part_one_answer

#Part Two
moves = [(0,0), (0,0)]
santa_coordinate = [0,0]
robot_coordinate = [0,0]
last_delivery = "robot"

for i in route:

    #Robot moves to deliver a present as according to the script
    if last_delivery == "santa":

        if i == "^":
            robot_coordinate[1] += 1

        elif i == "v":
            robot_coordinate[1] -= 1

        elif i == ">":
            robot_coordinate[0] += 1

        elif i == "<":
            robot_coordinate[0] -= 1

        else:
            raise ValueError("Unacceptable robot direction.")

        last_delivery = "robot"

    #Santa moves to deliver a present as according to the script
    else:

        if i == "^":
            santa_coordinate[1] += 1

        elif i == "v":
            santa_coordinate[1] -= 1

        elif i == ">":
            santa_coordinate[0] += 1

        elif i == "<":
            santa_coordinate[0] -= 1

        else:
            raise ValueError("Unacceptable santa direction.")

        last_delivery = "santa"

    moves += [(santa_coordinate[0], santa_coordinate[1]), (robot_coordinate[0], robot_coordinate[1])]

part_two_answer = len(set(moves))
print "Number of houses with at lest one present with robot (Part Two):", part_two_answer
