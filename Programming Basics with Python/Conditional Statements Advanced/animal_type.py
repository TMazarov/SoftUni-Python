animal_type = input()

mammal = ['dog']
reptiles = ['crocodile', 'tortoise', 'snake']

if animal_type in mammal:
    print("mammal")
elif animal_type in reptiles:
    print("reptile")
else:
    print("unknown")
    