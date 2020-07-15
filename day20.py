#Advent of Code December 20
#Written by C Shi - icydoge AT gmail dot com
#My input: 33100000

#Efficient get-all-factors courtesy of http://stackoverflow.com/a/6800214/5693062
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

puzzle_input = int(raw_input("Puzzle input: "))

#Part One
present_count = 0
house_number = int((puzzle_input/10) ** 0.5) #No less than this number required.

#Number if gifts in Part One is just ten times the sum of all factors, including the house_number itself and 1.
while present_count < (puzzle_input/10):
    house_number += 1
    present_count = sum(factors(house_number))

part_one_answer = house_number
print "Lowest house number to receive at least", puzzle_input, "gifts (Part One):", part_one_answer

#Part Two
present_count = 0.0
house_number = int((puzzle_input/11.0) ** 0.5)

#The samething, but we drop factors that is less than one-fiftieth of the house number.
while present_count < (puzzle_input/11.0):

    house_number += 1
    factors_of_number = factors(house_number)
    present_count = 0

    #Can probably be done with a sum on filter with a lambda, but not bothered.
    for n in factors_of_number:

        if float(house_number) / n <= 50.0:
            present_count += n

part_two_answer = house_number
print "Lowest house number to receive at least", puzzle_input, "gifts with changed rules (Part Two):", part_two_answer