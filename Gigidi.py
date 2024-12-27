from Enemy import *
import random


class Gigidi(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Gigidi",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print("*Gigidi Gigidi Gi gi di!*")

    def special_attack(self):
        did_special_work = random.random() < 0.50
        if did_special_work:
            self.health_points += 5
            print(f"Gigidi regenerated 5HP!")
