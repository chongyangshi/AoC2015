#Advent of Code December 21
#Written by icydoge - icydoge AT gmail dot com

import itertools
import math

weapons = [["Dagger", 8, 4], ["Shortsword", 10, 5], ["Warhammer", 25, 6], ["Longsword", 40, 7], ["Greataxe", 74, 8]]
armors = [["No Armor", 0, 0], ["Leather", 13, 1], ["Chainmail", 31, 2], ["Splintmail", 53, 3], ["Bandedmail", 75, 4], ["Platemail", 102, 5]]
rings = [["Empty Ring Slot 1", 0, 0, 0], ["Empty Ring Slot 2", 0, 0, 0], ["Damage +1", 25, 1, 0], ["Damage +2", 50, 2, 0], ["Damage +3", 100, 3, 0], ["Defense +1", 20, 0, 1], ["Defense +2", 40, 0, 2], ["Defense +3", 80, 0, 3]]

def get_damage(attacker_damage, defender_armor):

    damage = attacker_damage - defender_armor

    if damage < 1:
        damage = 1

    return damage


with open('inputs/rpg.txt') as f:
    content = f.read().splitlines()

boss_HP = int(content[0].split(' ')[2])
boss_damage = int(content[1].split(' ')[1])
boss_armor = int(content[2].split(' ')[1])

player_HP = 100
solutions = []
non_solutions = []

for weapon in weapons:
    for armor in armors:
        for ring_set in list(itertools.combinations(rings, 2)):
            player_damage = weapon[2] + sum([x[2] for x in ring_set])
            player_armor = armor[2] + sum([x[3] for x in ring_set])
            gold_expense = weapon[1] + armor[1] + sum([x[1] for x in ring_set])

            #Seems easy enough to formulate as a MMORPG player...
            if (math.ceil(float(player_HP) / float(get_damage(boss_damage, player_armor)))) >= (math.ceil(float(boss_HP) / float(get_damage(player_damage, boss_armor)))):
                solutions.append([weapon, armor, ring_set, gold_expense])

            else:
                non_solutions.append([weapon, armor, ring_set, gold_expense])

part_one_solution = min([x[3] for x in solutions])
print "Least amount of gold spent to kill the boss (Part One):", part_one_solution

part_two_solution = max([x[3] for x in non_solutions])
print "Most amount of gold to spend without killing the boss (Part Two):", part_two_solution
