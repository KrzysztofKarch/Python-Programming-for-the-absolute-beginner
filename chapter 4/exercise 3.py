# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 4, exercise 3
#
# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz podpowiedź - pierwsza litera słowa
tip = word[0]
# sprawdzenie czy podpowiedź została użyta
tip_on = False
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# utwórz 'pomieszaną' wersję słowa
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij grę
print(
"""
           Witaj w grze 'Wymieszane litery'!
        
   Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
(Aby uzyskać PODPOWIEDŹ, wpisz X)
"""
)
print("Zgadnij, jakie to słowo:", jumble)

guess = input("\nTwoja odpowiedź: ")

while guess != correct and guess != "":
    if guess.lower() == 'x':
        tip_on = True
        print("Pierwsza litera to:", tip)
        guess = input("Twoja odpowiedź: ")
    else:
        print("Niestety, to nie to słowo.")
        guess = input("Twoja odpowiedź: ")
    
if guess == correct and tip_on == False:
    print("Zgadza się! Zgadłeś! 10 punktów!\n")
if guess == correct and tip_on == True:
    print("Zgadza się! Zgadłeś! 5 punktów!\n")

print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
