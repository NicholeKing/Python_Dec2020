class Mario:
    # the initial method
    # all methods MUST have self in parameters
    def __init__(self):
        self.name = "Mario"
        self.pixel_width = 32
        self.pixel_height = 64
        self.hat_color = "red"
        self.has_mustache = True
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"pixel_width: {self.pixel_width}")
        print(f"pixel_height: {self.pixel_height}")
        print(f"hat_color: {self.hat_color}")
        print(f"has_mustache: {self.has_mustache}")
        print("***********")

m = Mario()
# print(m.name)
# print(m.hat_color)
m.show_stats()

# We can manually update a default set class with new values...
m2 = Mario()
m2.name = "Luigi"
# print(m2.name)
m2.hat_color = "green"
# print(m2.hat_color)

# ...But this is super inefficient. So let's make classes that accept parameters!

m2.show_stats()

# Found out the placement of this class in reference to the player class doesn't matter, but it DOES need to be before you try to create an instance of that object
class items:
    def __init__(self, name, ability, pw, ph, usable):
        self.name = name
        self.ability = ability
        self.pixel_width = pw
        self.pixel_height = ph
        self.usable = usable

# Our class that can take in a variety of parameters
class Player:
    def __init__(self, n, h_c, h_m, item):
        self.name = n
        self.pixel_width = 32
        self.pixel_height = 64
        self.hat_color = h_c
        self.has_mustache = h_m
        self.hold_item = item
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"pixel_width: {self.pixel_width}")
        print(f"pixel_height: {self.pixel_height}")
        print(f"hat_color: {self.hat_color}")
        print(f"has_mustache: {self.has_mustache}")
        print(f"Hold item: {self.hold_item.name}")
        print("***********")
    def jump(self):
        print(f"{self.name} jumped!")

fireball = items("Fireball", "Burns things", 20, 20, True)
p1 = Player("Wario", "yellow", True, fireball)

# print(p1.name)
# print(p1.pixel_width)

p1.show_stats()
# p1.jump()
# p1.jump()
# p1.jump()
wand = items("Wand", "Sparkles oooo", 15, 30, True)
p2 = Player("Peach", "None", False, wand)
# p2.jump()
p2.show_stats()