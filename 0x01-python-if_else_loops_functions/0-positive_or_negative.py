#!/usr/bin/python3
import random

random_number = random.randint(-10, 10)
if random_number < 0:
    print(f"{random_number} is negative")
elif random_number > 0:
    print(f"{random_number} is positive")
else:
    print(f"{random_number} is zero")
