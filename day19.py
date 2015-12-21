#Advent of Code December 19
#Written by icydoge - icydoge AT gmail dot com

from random import shuffle

def get_all_indices(input_string, search_string, offset):
    #Get all indices of the appearance of search_string in input_string, taken from Day 5.
    try:
        index = input_string.index(search_string) + offset

    except ValueError:
        return []

    return [index]+(get_all_indices(input_string[(index+len(search_string)-offset):], search_string, index+len(search_string)))


with open('inputs/molecules.txt') as f:
    content = f.read().splitlines()

#Separate replacement table and medicine molecule
medicine_molecule = content[-1]
content = content[:-2]

#Parse replacement table.
replacements = []
for line in content:
    replacement = line.split(" => ")
    replacements.append([replacement[0], replacement[1]])

#Part One
products = []
for replacement in replacements:
    
    occurrences = get_all_indices(medicine_molecule, replacement[0], 0)

    for i in occurrences:
        new_product = medicine_molecule[:i] + replacement[1] + medicine_molecule[i+len(replacement[0]):]
        products.append(new_product)

products_unique = list(set(products))
part_one_answer = len(products_unique)
print "Number of unique products (Part One):", part_one_answer

#Part Two
#I have given up on this one -- several different recursive methods didn't work, can't spend a day on this, so I went to the subreddit.
#Turns out for most data, apparently shuffle-and-retry of replacements work the fastest.
#Formatted solution courtesy of /u/What-A-Baller (https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4cu5b)
target = medicine_molecule
part_two_answer = 0

while target != 'e':

    target_copy = target

    for replacement in replacements:

        if replacement[1] not in target:
            continue

        target = target.replace(replacement[1], replacement[0], 1)
        part_two_answer += 1

    if target_copy == target:

        target = medicine_molecule
        part_two_answer = 0
        shuffle(replacements)

print "Number of steps to make the medcine (Part Two):", part_two_answer