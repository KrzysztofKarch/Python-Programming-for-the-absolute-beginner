# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 3, exercise 3

import random

print("Wymyśliłem liczbę 1-100, odgadnij ją. Masz 10 prób. \n")

number=random.randint(1,100)
trials=int(10)
guess=None

while guess!=number:
    guess=int(input("Podaj liczbę: "))
    trials-=1
    if guess>number:
        print("Za dużo")
    if guess<number:
        print("Za mało")
    if trials == 0:
        break
    
if guess == number:
    print("\nBrawo, zgadłeś, pozostala liczba prób:", trials, " prob.")
else:
    print("\nNie udalo Ci się odgadnąć w wyznaczonej liczbie prób. Chodziło o", number)
    
input()
    
