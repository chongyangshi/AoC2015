#Advent of Code December 4
#Written by icydoge - icydoge AT gmail dot com
#Brute force... Is there a better way?

import hashlib

input_string = raw_input("Enter puzzle input:")

number = 1
while True:
    new_hash = hashlib.md5(input_string+str(number)).hexdigest()
    if new_hash.startswith("00000"):
        part_one_answer = number
        break
    else:
        number += 1

print "Minimum number for key+number to start with 00000 (Part One):",part_one_answer

number = 1
while True:
    new_hash = hashlib.md5(input_string+str(number)).hexdigest()
    if new_hash.startswith("000000"):
        part_two_answer = number
        break
    else:
        number += 1

print "Minimum number for key+number to start with 000000 (Part Two):",part_two_answer