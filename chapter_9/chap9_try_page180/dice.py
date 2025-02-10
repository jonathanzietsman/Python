import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        print(random.randint(1, self.sides))
    
    def roll_multiple_times(self, rolls=10):
        for i in range(rolls):
            self.roll_die()

print("Rolling a 6-sided die:")
dice = Die()
dice.roll_multiple_times()
print()

print("Rolling a 10-sided die:")
dice = Die(10)
dice.roll_multiple_times(10)
print()


print("Rolling a 20-sided die:")
dice = Die(20)
dice.roll_multiple_times(10)
