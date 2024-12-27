from Enemy import *
import random


class Goblin(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Goblin",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("*Grumbling....*")

    def spread_disease(self):
        print("This Goblin is trying to spread infection.")

    def special_attack(self):
        did_special_work = random.random() < 0.20
        if did_special_work:
            self.attack_damage += 4
            print(f"Goblin gets angry and increases attack by 4")
