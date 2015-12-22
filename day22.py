#Advent of Code December 22
#Written by icydoge - icydoge AT gmail dot com
#Note: this is not a solution, but only the user-facing game simulation that requires human inputs.
#I played this game manually for around 25 minutes and found the lowest mana spent for Part One,  
#and the immediately higher rotation turned out to the the solution to Part Two.

spells = [["Magic Missile (M)", "M", 53], ["Drain (D)", "D", 73], ["Shield (S)", "S", 113], ["Poison (P)", "P", 173], ["Recharge (R)", "R", 229]]

def get_damage(attacker_damage, defender_armor):

    damage = attacker_damage - defender_armor

    if damage < 1:
        damage = 1

    return damage

with open('inputs/rpg2.txt') as f:
    content = f.read().splitlines()

boss_HP = int(content[0].split(' ')[2])
boss_damage = int(content[1].split(' ')[1])
boss_poison = 0

player_HP = 50
player_mana = 500
player_armor = 0
player_shield = 0
player_recharge = 0
mana_spent = 0

game_over = False
whos_turn = "Player"

while (not game_over):

    print ""
    print "========================================================="
    print "Round start."


    if player_recharge > 0:
        player_recharge -= 1
        player_mana += 101
        print "Player gains 101 mana from recharge, fading in", player_recharge, "rounds."

    print "Player HP:", player_HP, "Player Mana:", player_mana

    if player_shield > 0:
        player_shield -= 1
        player_armor = 7
        print "Player has 7 armor, fading in", player_shield, "rounds."

    else:
        player_armor = 0
        print "Player has 0 armor."

    if boss_poison > 0:
        boss_poison -= 1
        boss_HP -= 3
        print "Boss loses 3 HP due to poison, poison fading in", boss_poison, "rounds."

    if boss_HP <= 0:
        print "Boss is defeated."
        game_over = True
        continue

    print "Boss HP:", boss_HP

    if player_mana < 53:
        game_over = True
        print "Player lost due to running out of mana."
        continue

    print ""

    if whos_turn == "Player":

        available_moves = []

        for spell in spells:

            if spell[2] <= player_mana:

                if spell[1] == "S":
                    if player_shield > 0:
                        continue

                elif spell[1] == "P":
                    if boss_poison > 0:
                        continue

                elif spell[1] == "R":
                    if player_recharge > 0:
                        continue

                available_moves.append(spell[1])

        print "Available Spells:", available_moves
        player_action = ""
        while player_action not in available_moves:
            player_action = str(raw_input("Enter your action (single uppercase letter): "))

        if player_action == "M":
            player_mana -= 53
            mana_spent += 53
            boss_HP -= 4
            whos_turn = "Boss"
            continue

        if player_action == "D":
            player_mana -= 73
            mana_spent += 73
            boss_HP -= 2
            player_HP += 2
            whos_turn = "Boss"
            continue

        if player_action == "S":
            player_shield = 6
            player_mana -= 113
            mana_spent += 113
            whos_turn = "Boss"
            continue

        if player_action == "P":
            boss_poison = 6
            player_mana -= 173
            mana_spent += 173
            whos_turn = "Boss"
            continue

        if player_action == "R":
            player_recharge = 5
            player_mana -= 229
            mana_spent += 229
            whos_turn = "Boss"
            continue

    elif whos_turn == "Boss":

        damage = get_damage(boss_damage, player_armor)
        player_HP -= damage
        print "Boss does", damage, "damage to player; player HP is now", player_HP
        if player_HP <= 0:
            game_over = True
            print "Player is defeated due to lack of HP."
        whos_turn = "Player"
        continue


print "Total mana spent =", mana_spent




