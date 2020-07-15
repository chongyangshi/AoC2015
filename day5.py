#Advent of Code December 5
#Written by C Shi - icydoge AT gmail dot com

def get_all_indices(input_string, search_string, offset):
    #Get all indices of the appearance of search_string in input_string
    try:
        index = input_string.index(search_string) + offset
    except ValueError:
        return []
    return [index]+(get_all_indices(input_string[(index+len(search_string)-offset):], search_string, index+len(search_string)))

with open('inputs/naughty-nice-strings.txt') as f:
    content = f.read().splitlines()

nice_strings = []
naughty_strings = []

#Part One
for pstring in content:

    #Check for disallowed string patterns
    disallowed_patterns_discovered = False
    disallowed_patterns = ["ab", "cd", "pq", "xy"]
    for pattern in disallowed_patterns:
        if pattern in pstring:
            naughty_strings.append(pstring)
            disallowed_patterns_discovered = True
            break
    if disallowed_patterns_discovered:
        continue

    #If no disallowed patterns, scan for replicates and three vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    if pstring[0] in vowels:
        vowels_found = [pstring[0]]
    else:
        vowels_found = []

    pairs = []
    prev_letter = pstring[0]
    for i in range(1, len(pstring)):

        if pstring[i] in vowels:
            vowels_found.append(pstring[i])

        if pstring[i] == prev_letter:
            pair = pstring[i] + prev_letter
            if pair not in pairs:
                pairs.append(pair)

        prev_letter = pstring[i]

    if (len(vowels_found) >= 3) and (len(pairs) >= 1):
        nice_strings.append(pstring)
    else:
        naughty_strings.append(pstring)

part_one_answer = len(nice_strings)
print "Number of strings that are nice (Part One):", part_one_answer

nice_strings = []
naughty_strings = []

#Part Two
for pstring in content:

    #Check with the second rule first
    if len(pstring) < 3: #Will not fit the first rule
        naughty_strings.append(pstring)
        continue

    has_one_between_two = False
    first_letter = pstring[0]
    second_letter = pstring[1]
    third_letter = pstring[2]

    if first_letter == third_letter:
        has_one_between_two = True
    else:
        for i in range(1,len(pstring)-2):
            first_letter = pstring[i]
            second_letter = pstring[i+2]
            third_letter = pstring[i+2]
            if first_letter == third_letter:
                has_one_between_two = True
                break
        if not has_one_between_two:
            naughty_strings.append(pstring) #Does not have one letter between any two same letters
            continue 
    
    #Then check the first rule by searching
    nice_string_found = False

    for j in range(0,len(pstring)-1):
        search_string = pstring[j]+pstring[j+1]
        indices = get_all_indices(pstring, search_string, 0)

        if len(indices) > 1:
            for i in range(0,len(indices)-1):
                if (indices[i+1] - indices[i]) > 1: #non-overlapping
                    nice_string_found = True
                    break

        if nice_string_found:
            break

    if nice_string_found:
        nice_strings.append(pstring)
    else:
        naughty_strings.append(pstring)

part_two_answer = len(nice_strings)
print "Number of strings that are nice with modified requirements (Part Two):", part_two_answer



