#Advent of Code December 15
#Written by C Shi - icydoge AT gmail dot com
#Trust me, this is exactly not the way I want to do it.
#However, I am short on time today, and an attempt with scipy.optimize has failed.
#Might come back to this later, but brute force is the best I can write 
#with limited time today, without consulting other solutions.

def calc(a, b, c, d, ingredients):
    #Calculate the score
    capacity = max(0, ingredients[0][1] * a + ingredients[1][1] * b + ingredients[2][1] * c + ingredients[3][1] * d)
    durability = max(0, ingredients[0][2] * a + ingredients[1][2] * b + ingredients[2][2] * c + ingredients[3][2] * d)
    flavour = max(0, ingredients[0][3] * a + ingredients[1][3] * b + ingredients[2][3] * c + ingredients[3][3] * d)
    texture = max(0, ingredients[0][4] * a + ingredients[1][4] * b + ingredients[2][4] * c + ingredients[3][4] * d)
    calories = ingredients[0][5] * a + ingredients[1][5] * b + ingredients[2][5] * c + ingredients[3][5] * d
    return [capacity * durability * flavour * texture, calories]

with open('inputs/ingredients.txt') as f:
    content = f.read().splitlines()

#Parse input into ingredients
ingredients = []
for item in content:
    line = item.split(' ')
    ingredients.append([line[0][:-1], int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])])

#Brute force score and calories calculation
scores = []
calories = []
for a in range(0, 101):
    for b in range(0, 101-a):
        for c in range(0, 101-a-b):
            d = 100 - a - b - c
            result = calc(a, b, c, d, ingredients)
            score = result[0]
            if score != 0:
                cookie_calories = result[1]
                scores.append(score)
                calories.append(cookie_calories)

#Part One
part_one_answer = max(scores)
print "Maximum possible score (Part One):", part_one_answer


#Part Two
best_500_calories_score = -1

for i in range(0, len(calories)):
    if calories[i] == 500:
        if scores[i] > best_500_calories_score:
            best_500_calories_score = scores[i]
part_two_answer = best_500_calories_score 

print "Best possible score with 500 calories (Part Two):", part_two_answer
