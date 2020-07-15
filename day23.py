#Advent of Code December 23
#Written by C Shi - icydoge AT gmail dot com
#Thanks, Freeman.


def execute(program, registers):

    program_counter = 0

    while program_counter < len(program):

        line = program[program_counter].split(' ')

        if line[0] == "hlf":
            registers[line[1]] = registers[line[1]]/2
            program_counter += 1

        elif line[0] == "tpl":
            registers[line[1]] = registers[line[1]] * 3
            program_counter += 1

        elif line[0] == "inc":
            registers[line[1]] += 1
            program_counter += 1

        elif line[0] == "jmp":
            program_counter += int(line[1])

        elif line[0] == "jie":

            if registers[line[1][:-1]] % 2 == 0:
                program_counter += int(line[2])

            else:
                program_counter += 1

        elif line[0] == "jio":

            if registers[line[1][:-1]] == 1:
                program_counter += int(line[2])

            else:
                program_counter += 1

        else:
            raise ValueError("Unidentified instruction.")

    return registers


with open('inputs/assembly.txt') as f:
    content = f.read().splitlines()

#Part One
registers = {'a': 0, 'b': 0}
part_one_answer = execute(content, registers)['b']
print "Value in register b after execution (Part One):", part_one_answer

#Part Two
registers = {'a': 1, 'b': 0}
part_two_answer = execute(content, registers)['b']
print "Value in register b after execution, with a starting from 1 (Part Two):", part_two_answer


