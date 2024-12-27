from Enemy import *
from Goblin import *
from Gigidi import *
from Hero import *
from Weapon import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("--------------------------------------------------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        e1.attack()
        e2.health_points -= e1.attack_damage
        e2.attack()
        e1.health_points -= e2.attack_damage
    print("--------------------------------------------------------")

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy()} won the battle!")
    else:
        print(f"{e2.get_type_of_enemy()} won the battle!")


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.talk()

    while hero.health_points > 0 and enemy.health_points > 0:
        print("--------------------------------------------------------")

        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        hero.attack()
        enemy.health_points -= hero.attack_damage
        enemy.attack()
        hero.health_points -= enemy.attack_damage
    print("--------------------------------------------------------")

    if hero.health_points > 0:
        print(f"Hero won the battle!")
    else:
        print(f"{enemy.get_type_of_enemy()} won the battle!")


goblin = Goblin(10, 1)
gigidi = Gigidi(20, 3)
hero = Hero(15, 2)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, gigidi)


# print(
#     f"{goblin.get_type_of_enemy()} has {goblin.health_points} health points and can do attack of {goblin.attack_damage} damage"
# )
# print(
#     f"{gigidi.get_type_of_enemy()} has {gigidi.health_points} health points and can do attack of {gigidi.attack_damage} damage"
# )
