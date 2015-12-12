#Advent of Code December 11
#Written by icydoge - icydoge AT gmail dot com

def increment(input_string):

    input_string = list(input_string.lower())
    letters = map(chr,range(97,123)) #Get lower case alphabet in a list

    if input_string[-1] != 'z':
        input_string[-1] = letters[letters.index(input_string[-1])+1] #Increment the left-most letter if it's not z
    else:
        i = len(input_string) - 1
        input_string[i] = 'a'

        while i>0:  #Try to wrap around each letter to the left, until success (none-z) or exhaustion
            if input_string[i-1] == 'z':
                input_string[i-1] = 'a'
                i -= 1
            else:
                input_string[i-1] = letters[letters.index(input_string[i-1])+1]
                break
            
    return "".join(input_string)

def password_check(input_string):

    input_string = list(input_string.lower())
    disallowed_letters = ['i', 'o', 'l']

    if len(input_string) != 8:
        print "Password","".join(input_string),"failed due to length."
        return False

    if set(disallowed_letters).intersection(input_string):
        print "Password","".join(input_string),"failed due to disallowed letters."
        return False

    has_straight_three = False
    has_two_pairs = False

    prev_letter = input_string[0]
    pairs = []

    for i in range(1,8): 

        if input_string[i] == prev_letter: #Found a pair
            pair = input_string[i]+prev_letter
            if pair not in pairs: #Check if the same pair is already known, if not, remember the discovered pair
                pairs.append(pair)

        elif ord(input_string[i]) == (ord(prev_letter) + 1):  #The letter is in increasing straight of the previous
            if i < 7:
                if ord(input_string[i]) == (ord(input_string[i+1]) - 1): #Next letter is in increasing straight of this letter
                    has_straight_three = True

        prev_letter = input_string[i]

    if len(pairs) >= 2:
        has_two_pairs = True

    if (not has_straight_three) or (not has_two_pairs):
        print "Password","".join(input_string),"failed due to lack of straights or pairs."
        return False

    return True


input_string = raw_input("Enter puzzle input:")
if not input_string.isalpha():
    raise ValueError("Input is not a string of letters.")
input_string = input_string.lower()

#This while loop is guaranteed to terminate by finding a qualifying password, due to the aaaaaaaa-zzzzzzzz loop, as per the problem requirements.
#A formal proof for the guarantee of termination is an exercise for the reader :)
while (not password_check(input_string)): 
    input_string = increment(input_string)

part_one_answer = input_string

input_string = increment(part_one_answer)
while (not password_check(input_string)):
    input_string = increment(input_string)
part_two_answer = input_string
print "==========================================="
print "Next password (Part One):",part_one_answer
print "Next password after expiry (Part Two):",part_two_answer