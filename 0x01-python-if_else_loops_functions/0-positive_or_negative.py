#!/usr/bin/python3
import random

random_number = random.randint(-100, 100)
if random_number < 0:
    print(f"{random_number} is negative")
elif random_number > 0:
    print(f"{random_number} is positive")
else:
    print(f"{random_number} is zero")
