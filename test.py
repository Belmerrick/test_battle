import random

total_enemy_damage = 0
enemy_health = 20
player_level = 1
player_health = 40 + (player_level * 5)
number_of_potions = 2
levelup_xp = 100
total_player_xp = 0
enemy_xp = 20


print("")

while player_level < 10:
    weapon_damage = 0
    damage = random.randint(2, 5) + (player_level - 1) + weapon_damage
    enemy_damage = random.randint(1, 3)
    player_crit_damage = damage * 2
    player_crit_chance = random.randint(1, 100)
    enemy_crit_damage = enemy_damage * 2
    enemy_crit_chance = random.randint(1, 100)
    new_weapon = random.randint(1, 20)
    if player_crit_chance >= 90:
        enemy_health -= player_crit_damage
        print("you crit the slime for", player_crit_damage, "damage!")
        print("the slime's health is", enemy_health)
        print("")
    elif enemy_health > 0:
        enemy_health -= damage
        print("you did", damage, "damage to Slime")
        print("the slime's health is", enemy_health)
        print("")
    if enemy_health <= 0:
        enemy_health += 20
        total_player_xp += 20
        print("You defeated the slime and gained", enemy_xp, "experience!")
        print("your total xp is", total_player_xp)
        if new_weapon == 1:
            if weapon_damage < 5:
                weapon_damage = 5
                print("You gained a Legendary weapon! The weapon does", weapon_damage, "extra damage!")
                print("")
            else:
                print("You did not find a weapon")
                print("")
        elif 2 <= new_weapon <= 4:
            if weapon_damage < 4 and weapon_damage != 5:
                weapon_damage = 4
                print("You gained an epic weapon! The weapon does", weapon_damage, "extra damage!")
                print("")
            else:
                print("You did not find a weapon")
                print("")
        elif 4 < new_weapon <= 7:
            if weapon_damage < 3 and weapon_damage != 4 or 5:
                weapon_damage = 3
                print("You gained a rare weapon! The weapon does", weapon_damage, "extra damage!")
                print("")
            else:
                print("You did not find a weapon")
                print("")
        elif 7 < new_weapon <= 10:
            if weapon_damage < 2 and weapon_damage != 3 or 4 or 5:
                weapon_damage = 2
                print("You gained an uncommon weapon! The weapon does", weapon_damage, "extra damage!")
                print("")
            else:
                print("You did not find a weapon")
                print("")
        elif 10 < new_weapon <= 14:
            if weapon_damage < 1 and weapon_damage != 2 or 3 or 4 or 5:
                weapon_damage = 1
                print("You gained a common weapon! The weapon does", weapon_damage, "extra damage!")
                print("")
            else:
                print("You did not find a weapon")
                print("")
        else:
            print("You did not find a weapon")
            print("")
    if total_player_xp >= levelup_xp:
        total_player_xp -= 100
        player_level += 1
        print("you have gained a level! you are now level", player_level, "!")
        print("")
        if player_health < 40 + (player_level * 5):
            player_health = 40 + (player_level * 5)
            print("your new health is", player_health)
        if player_level == 10:
            break
    if enemy_crit_chance >= 95:
        player_health -= enemy_crit_damage
        total_enemy_damage += enemy_crit_damage
        print("the slime crit you for", enemy_crit_damage, "damage!")
        print("your health is", player_health)
        print("")
    elif player_health > 0:
        player_health -= enemy_damage
        total_enemy_damage += enemy_damage
        print("The SLIME did", enemy_damage, "to you!")
        print("your health is", player_health)
        print("")
    if total_enemy_damage >= (40 + (player_level * 5)) * 0.8:
        if number_of_potions > 0:
            number_of_potions -= 1
            player_health += 10
            print("You used a potion and gained 10 health!")
            print("your health is", player_health)
    if player_health <= 0:
        print("You have been defeated by a Slime!")
        break
