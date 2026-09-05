import random
#Random Module

#return random float between 0.0 to 1.0 (excluded)
print(random.random())
print("\n")

#return random int between a and b
print(random.randint(1,10))
print("\n")

#choice(sequence)-return a random item from sequence
l=[1,2,3,4,7]
print(random.choice(l))
print("\n")

#shuffle(sequence)-returns the element shuffle in random order
random.shuffle(l)
print(l)

