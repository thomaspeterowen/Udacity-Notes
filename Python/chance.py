import random

def coin_flip():
    return random.choice(['heads','tails'])

def dice_roll():
    return random.randint(1, 6)