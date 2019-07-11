# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 3, exercise 4

import random

number = int(input("Wprowadź liczbę od 1 do 100, którą komputer będzie zgadywał: "))

minimum = int(1)
maximum = int(100)

guess = int((maximum + minimum ) // 2)
print("\nZgaduje:", guess)

while guess != number:
    if guess > number:
        maximum = guess - 1
    elif guess < number:
        minimum = guess + 1
    guess = (maximum + minimum ) // 2
    print("Zgaduje:", guess)

print("\nBrawo! Zgadłem! ")
input()
