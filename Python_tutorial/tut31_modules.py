from random import random
import random

random_number = random.randint(0,5)
print(random_number+1)

lst = ["sani", "shubha", "rohit"]
choice = random.choice(lst)
print(choice)

if choice == "sani":
    print("This is Sani")