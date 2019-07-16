# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 4, exercise 4

import random

WORDS=("statua","krokodyl","marmur","klawiatura","auto","python")
word=random.choice(WORDS)
letters_yes = ()
letters_no = ()

print(""""*** Odgadnij słowo - tylko rzeczowniki ***

"Zasady: możesz 5 razy zapytać czy dana litera znajduje się w słowie,
         potem będziesz musiał je odgadnąć. """)


print("\n Liczba liter wylosowanego słowa:", len(word))

for i in range(5):
    letter = input("Podaj literę: ")
    if letter in word:
        print("litera występuje")
        letters_yes += (letter,)
    else:
        print("brak litery")
        letters_no += (letter,)

print("\nLitery występujące: ", end="")
for i in letters_yes:
    print(i, end=" ")
print("\nLitery niewystępujące: ", end="")
for i in letters_no:
    print(i, end=" ")

guess = input("\n\nTwoja odpowiedź: ")

if guess == word:
    print("Brawo! Zgadłeś. ")
else:
    print("Niestety, nie udało Ci się. Chodziło o słowo", word)

input()
