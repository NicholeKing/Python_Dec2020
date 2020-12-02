import random
# SMASH BROS ON THE CONSOLE (not that one)

# Class for playable characters
    # punch -
    # jump -
    # damage_percentage -
    # special_attack -
    # shield -
    # name -
    # color -
    # lives -

class Player:
    def __init__(self, name, color, lives, special_attack):
        self.name = name
        self.color = color
        self.lives = lives
        self.damage_percent = 0
        self.special = special_attack
        self.block = False
    def enter_player(self):
        print(f"New challenger, {self.name}, has appeared!")
    def punch(self, target):
        if target.lives <= 0:
            print("He's already dead!")
        else:
            if target.block:
                print(f"{target.name} avoided {self.name}'s punch!")
                target.block = False
            else:
                target.damage_percent += 10
                print(f"{self.name} punches {target.name}!")
                target.calculate_odds()
    def activate_shield(self):
        print(f"{self.name} activated shield!")
        self.block = True
    def dodge(self):
        print(f"{self.name} jumps into the air!")
        self.block = True
    def calculate_odds(self):
        odds = self.damage_percent * random.random()
        if odds >= 150:
            print(f"{self.name} lost a life!")
            if self.lives > 0:
                self.lives -= 1
                self.damage_percent = 0
                self.death()
    def death(self):
        if self.lives == 0:
            print(f"FATALITY!! {self.name} has died!")
    def special_atk(self, target):
        if target.lives <= 0:
            print("He's already dead!")
        else:
            if target.block:
                print(f"{target.name} took half damage from {self.name}'s special attack!")
                target.damage_percent += 25
                target.block = False
                target.calculate_odds()
            else:
                target.damage_percent += 50
                print(f"{self.name} used {self.special} on {target.name}!")
                target.calculate_odds()

pikachu = Player("Pikachu", "original", 3, "Thunderbolt")
link = Player("Link", "original", 3, "Arrow")
kirby = Player("Kirby", "original", 3, "Copy")
ness = Player("Ness", "original", 3, "PK Thunder")

# Select random stage
stages = ["Saffron City", "Hyrule Castle", "Death Star", "Corneria", "Final Destination", "Pokemon Arena", "DK's House", "The Coding Dojo", "Yoshi's Island", "PokeFloats", "Andy's Bedroom"]

def select_stage():
    rand = random.random() * len(stages)
    print(f"You are fighting in {stages[round(rand)]}!!")

# pikachu.enter_player()
# link.enter_player()
# pikachu.punch(link)
# pikachu.punch(link)
# link.dodge()
# pikachu.punch(link)
# pikachu.punch(link)
# link.activate_shield()
# pikachu.punch(link)
# pikachu.punch(link)
# pikachu.punch(link)
# print(link.damage_percent)

# while link.lives > 0:
#     pikachu.punch(link)

select_stage()

# ness.special_atk(kirby)
# ness.special_atk(kirby)
# kirby.dodge()
# ness.special_atk(kirby)
# kirby.activate_shield()
# ness.special_atk(kirby)