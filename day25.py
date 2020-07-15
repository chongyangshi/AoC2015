#Advent of Code December 25
#Written by C Shi - icydoge AT gmail dot com

with open('inputs/machine.txt') as f:
    content = f.read().splitlines()[0].split(' ')

code_row = int(content[-3][:-1])
code_col = int(content[-1][:-1])

code = 20151125
row_number = 2
col_number = 1 #Start from (2,1) due to Python not having do while.
diagonal_width = 2
current_width = 1

while True:

    #Transform the code.
    code = (code * 252533) % 33554393

    #Correct code found.
    if (row_number == code_row) and (col_number == code_col):
        part_one_answer = code
        break

    #Wrap around when end of diagonal reached.
    if current_width == diagonal_width:
        diagonal_width += 1
        current_width = 1     
        row_number = col_number + 1
        col_number = 1

    #Increment on the diagonal.
    else:
        current_width += 1
        row_number -= 1
        col_number += 1

print "Code for the input location is (Part One):", part_one_answer
print "Part Two: Congratulations, we have finished Advent of Code 2015!"
