#Advent of Code December 8
#Written by C Shi - icydoge AT gmail dot com

with open('inputs/strings.txt') as f:
    content = f.read().splitlines()[:-1]

content_for_encode = content 

total_original_length = 0
total_string_length = 0

for i in range(0,len(content)):

    total_original_length += len(content[i])

    #Remove quote marks from two ends of each line
    if (content[i][0] == '\"') and (content[i][-1] == '\"'):
        content[i] = content[i][1:-1]
    
    #"Parse" the line
    line_length = 0
    j = 0
    while j<len(content[i]):
        if (content[i][j] == '\\') and (content[i][j+1] == 'x'): #Assuming legal input provided by the question, otherwise will need to have additional checks for list index
            line_length += 1
            j += 4
        elif (content[i][j] == '\\') and (content[i][j+1] == '\"'):
            line_length += 1
            j += 2
        elif (content[i][j] == '\\') and (content[i][j+1] == '\\'):
            line_length += 1
            j += 2
        else:
            line_length += 1
            j += 1

    total_string_length += line_length

part_one_result = total_original_length - total_string_length
print "Original Length - Total String Length (Part One): ", part_one_result

total_encoded_length = 0
for i in range(0,len(content_for_encode)):

    j = 0
    line_len = len(content_for_encode[i])

    encoded_string = "\"\\\""  #Assuming legal input, with quotes on each side
    while j < line_len:
        if (content_for_encode[i][j] == '\\') and (content_for_encode[i][j+1] == '"'):
            encoded_string += "\\\\\\\""
            j += 2
        elif (content_for_encode[i][j] == '"'):
            encoded_string += "\\\""
            j += 1
        elif (content_for_encode[i][j] == '\\') and (content_for_encode[i][j+1] == '\\'):
            encoded_string += "\\\\\\\\"
            j += 2
        elif (content_for_encode[i][j] == '\\') and (content_for_encode[i][j+1] == 'x'):
            encoded_string += "\\\\"
            j += 1
        else:
            encoded_string += content_for_encode[i][j]
            j += 1
    encoded_string += "\\\"\""
    
    total_encoded_length += len(encoded_string) 

part_two_result = total_encoded_length - total_original_length
print "Total Encoded Length - Original Length (Part Two): ", part_two_result
