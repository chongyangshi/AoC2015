#Advent of Code December 12
#Written by C Shi - icydoge AT gmail dot com

import json

def has_value(dicti, item):
    #Returns true if the dictionary dicti has value item in one of the keys, false otherwise.
    contain_item = False

    for i in dicti:
        if dicti[i] == item:
            contain_item = True

    return contain_item


def json_sum(JSONData, exclude_red):
    #Recursive search and sum in the input's data structure.

    if isinstance(JSONData,unicode):
        return 0

    elif isinstance(JSONData, int):
        return JSONData

    elif isinstance(JSONData, list):
        return sum(json_sum(x, exclude_red) for x in JSONData)

    elif isinstance(JSONData, dict):

        if exclude_red and has_value(JSONData, u'red'):
            return 0

        sum_value = 0
        for i in JSONData:
            
            if isinstance(JSONData[i], int):
                sum_value += JSONData[i]
            else:
                sum_value += json_sum(JSONData[i], exclude_red)

        return sum_value


with open('inputs/accounting.json') as JSONFile:
    JSONData = json.load(JSONFile)

part_one_result = json_sum(JSONData, False)
print "Sum of accounting data (Part One):",part_one_result

part_two_result = json_sum(JSONData, True)
print "Sum of accounting data excluding red (Part Two):",part_two_result