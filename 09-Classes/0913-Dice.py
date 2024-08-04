from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def rell_die(self):
        return randint(1, self.sides)


for _ in range(10):
    die = Die()
    print(die.rell_die())
print("\n")

for _ in range(10):
    die = Die(10)
    print(die.rell_die())
print("\n")


for _ in range(10):
    die = Die(20)
    print(die.rell_die())
print("\n")
