# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 3, exercise 2

import random

print("Wyniki 100 rzutow monetą. ")

throw = int(0)
head = int(0)
tail = int(0)
while throw < 100:
    flip = random.randint(0, 1)
    if flip == 1:
        head += 1
    else:
        tail += 1
    throw += 1

print("Orzel:", tail)
print("Reszka:", head)
input()
