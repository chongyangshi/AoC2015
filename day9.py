#Advent of Code December 9
#Written by C Shi - icydoge AT gmail dot com
#Implementing TSP algorithm

def get_dict_min(dicti, disjoint_list):
    #Get the minimum key value in dicti where the key is not in disjoint_list
    minkey = ''
    minvalue = None
    for item in dicti:
        if item not in disjoint_list:

            if minvalue == None:
                minkey = item
                minvalue = dicti[item]

            else:
                if dicti[item] < minvalue:
                    minkey = item
                    minvalue = dicti[item]

    if minvalue != None:
        return [minkey, minvalue]
    else:
        raise ValueError("Disjoint list covers the whole route map.")
        #Should never happen on legal input.

def get_dict_max(dicti, disjoint_list):
    #Get the maximum key value in dicti where the key is not in disjoint_list
    maxkey = ''
    maxvalue = None
    for item in dicti:
        if item not in disjoint_list:

            if maxvalue == None:
                maxkey = item
                maxvalue = dicti[item]

            else:
                if dicti[item] > maxvalue:
                    maxkey = item
                    maxvalue = dicti[item]

    if maxvalue != None:
        return [maxkey, maxvalue]
    else:
        raise ValueError("Disjoint list covers the whole route map.")
        #Should never happen on legal input.

def get_route_distance(distance_map, route):
    distance = 0
    for i in range(0,len(route)-1):
        distance += int(distance_map[route[i]][route[i+1]])
    return [route, distance]

with open('inputs/routes.txt') as f:
    content = f.read().splitlines()[:-1]

#Construct the table
distance = {}
for edge in content:
    line = edge.split(' ')
    #Build 2-D dictionary (distance table) in both directions

    if line[0] in distance:
        distance[line[0]][line[2]] = int(line[4])
    else:
        distance[line[0]] = {}
        distance[line[0]][line[2]] = int(line[4])

    if line[2] in distance:
        distance[line[2]][line[0]] = int(line[4])
    else:
        distance[line[2]] = {}
        distance[line[2]][line[0]] = int(line[4])

nodes = distance.keys();

#Get minimum distance
all_routes = []
for node in nodes:
    route = [node]

    while (len(route) < len(distance)):
        route.append(get_dict_min(distance[route[-1]], route)[0])

    all_routes.append(route)

part_one_answer = min(get_route_distance(distance, route)[1] for route in all_routes)
print "Shortest distance (Part One) is:",part_one_answer

#Get maximum distance
all_routes = []
for node in nodes:
    route = [node]

    while (len(route) < len(distance)):
        route.append(get_dict_max(distance[route[-1]], route)[0])

    all_routes.append(route)

part_two_answer = max(get_route_distance(distance, route)[1] for route in all_routes)
print "Longest distance (Part Two) is:",part_two_answer