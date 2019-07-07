# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 3, exercise 1

import random

print("\t*** Wrozba na dzis ***")
input("\nNacisnij Enter\n")

case=random.randint(1,5)

if case==1:
    print("Ojej, zginiesz za 2 godziny, lepiej nie wychodź z domu. ")
elif case==2:
    print("Zginiesz jutro. ")
elif case==3:
    print("Może zginiesz, może nie. ")
elif case==4:
    print("Wygrasz na loteri, o ile dobrze obstawisz. ")
elif case==5:
    print("Czeka Cię niespodzianka. ")
else:
    print("Ups, coś poszło nie tak. ")

input()
