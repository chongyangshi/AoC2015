#Advent of Code December 10
#Written by icydoge - icydoge AT gmail dot com

def operate(pinput):
    poutput = ""
    prev = pinput[0]
    count = 1
    for i in range(1,len(pinput)):
        if pinput[i] == prev:
            count += 1
        else:
            poutput += str(count) + prev
            prev = pinput[i]
            count = 1
    poutput += str(count) + prev #Tailing sequence.
    return poutput


input_string = raw_input("Enter puzzle input:")
try:
    int(input_string)
except ValueError:
    raise ValueError("Input is not a string of digits.")

part_one_answer = str(input_string)
part_two_answer = str(input_string)

for i in range(40):
    part_one_answer = operate(part_one_answer)
print "Length after 40 operations (Part One):",len(part_one_answer)

for i in range(50):
    part_two_answer = operate(part_two_answer)
print "Length after 50 operations (Part Two):",len(part_two_answer)