#Advent of Code December 14
#Written by C Shi - icydoge AT gmail dot com

def reindeer_fly(reindeer, time):
    #Give the distance the reindeer covered until that time
    cycles = time / (reindeer[2] + reindeer[3])
    remainder = time % (reindeer[2] + reindeer[3])
    distance = cycles * reindeer[1] * reindeer[2] #Distance travelled in full fly-break cycles

    #Distance travelled in the remainder time
    if remainder <= reindeer[2]:
        distance += remainder * reindeer[1]
    else:
        distance += reindeer[2] * reindeer[1]

    return distance

def look_up_reindeer(name, reindeers):
    #Return the index for the reindeer with that name
    for reindeer in reindeers:

        if reindeer[0] == name:
            return reindeers.index(reindeer)

with open('inputs/reindeer.txt') as f:
    content = f.read().splitlines()

reindeers = []
for reindeer in content:
    line = reindeer.split(' ')
    reindeers.append([line[0], int(line[3]), int(line[6]), int(line[13])])

#Part One
fly_time = 2503
best_distance = -1
for reindeer in reindeers:
    if reindeer_fly(reindeer, fly_time) > best_distance:
        best_distance = reindeer_fly(reindeer, fly_time)

part_one_answer = best_distance
print "Distance the winning reindeer travelled (Part One):", part_one_answer

#Part Two
for reindeer in reindeers:
    reindeer.append(0) #points

for t in range(1, fly_time+1):

    best_distance = -1
    best_reindeers = []
    
    for reindeer in reindeers:

        flying = reindeer_fly(reindeer, t)

        if flying > best_distance: #Only one reindeer in the lead
            best_distance = flying
            best_reindeers = [reindeer[0]]

        elif flying == best_distance: #multiple reindeers in the lead
            best_reindeers.append(reindeer[0]) 

    for i in best_reindeers:
        reindeers[look_up_reindeer(i,reindeers)][4] += 1 #Add point to reindeer(s) in the lead.

#Find the reindeer with the highest point
highest_point = -1
for reindeer in reindeers:
    if reindeer[4] > highest_point:
        highest_point = reindeer[4]

part_two_answer = highest_point
print "Points of the winning reindeer (Part Two):", part_two_answer

