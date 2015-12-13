#Advent of Code December 7, with dynamic planning
#Written by icydoge - icydoge AT gmail dot com
#Updated to include result for Part Two.

def intval(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def process_gate(target, content, target_list):
    global value_table

    if intval(target):
        return int(target)

    input = content[target_list.index(target)]

    input_exploded = input.split(' ')

    if input_exploded[1] == "->":  #either wire-wire or number-wire
        if intval(input_exploded[0]):
            result = int(input_exploded[0])
            value_table[input_exploded[-1]] = result
            return result #number
        else:
            result = process_gate(input_exploded[0], content, target_list)
            value_table[input_exploded[-1]] = result
            return result #another wire

    elif input_exploded[0] == "NOT": #NOT gate
        if input_exploded[1] in value_table:
            return ~value_table(input_exploded[1])
        else:
            result = ~process_gate(input_exploded[1], content, target_list)
            value_table[input_exploded[-1]] = result
            return result

    elif input_exploded[1] == "AND": #AND gate

        if input_exploded[0] in value_table:
            left = value_table[input_exploded[0]]
        else:
            left = process_gate(input_exploded[0], content, target_list)

        if input_exploded[2] in value_table:
            right = value_table[input_exploded[2]]
        else:
            right = process_gate(input_exploded[2], content, target_list)
        result = left & right
        value_table[input_exploded[-1]] = result
        return result

    elif input_exploded[1] == "OR": #OR gate

        if input_exploded[0] in value_table:
            left = value_table[input_exploded[0]]
        else:
            left = process_gate(input_exploded[0], content, target_list)

        if input_exploded[2] in value_table:
            right = value_table[input_exploded[2]]
        else:
            right = process_gate(input_exploded[2], content, target_list)
        result = left | right
        value_table[input_exploded[-1]] = result
        return result

    elif input_exploded[1] == "LSHIFT": #LSHIFT operation
        if intval(input_exploded[2]):
            if input_exploded[2] in value_table:
                return value_table[input_exploded[2]] << int(input_exploded[2])
            else:
                result = process_gate(input_exploded[0], content, target_list) << int(input_exploded[2])
                value_table[input_exploded[-1]] = result
                return result
        else:
            raise ValueError("Invalid LSHIFT value.")

    elif input_exploded[1] == "RSHIFT": #RSHIFT operation
        if intval(input_exploded[2]):
            if input_exploded[2] in value_table:
                return value_table[input_exploded[2]] >> int(input_exploded[2])
            else:
                result = process_gate(input_exploded[0], content, target_list) >> int(input_exploded[2])
                value_table[input_exploded[-1]] = result
                return result
        else:
            raise ValueError("Invalid RSHIFT value.")

    else:
        raise ValueError("Unexpected operation!")

target_list = []
value_table = {}

with open('puzzle.txt') as f:
    content = f.read().splitlines()

for i in range(0,len(content)):
    row = content[i].split(' ')
    target_list.append(row[-1])

if target_list[-1] == '':
    target_list = target_list[:-1]
    content = content[:-1]
    #strip last empty line if present

part_one_result = process_gate("a", content, target_list)
print "Result for Part One: ",part_one_result

content[target_list.index("b")] = str(part_one_result) + " -> b"
value_table = {} #reset lookup table
part_two_result = process_gate("a", content, target_list)
print "Result for Part Two: ",part_two_result

