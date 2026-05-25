import random

random_coin_flip = random.randint(0, 1)
if random_coin_flip == 1:
    print("Heads")
else:
    print("Tails")
print(random_coin_flip)