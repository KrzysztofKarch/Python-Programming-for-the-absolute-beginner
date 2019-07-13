# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 4, exercise 2

print("Program wypisujący komunikat wspak. \n")

statement=input("Wprowadź komunikat: ")

# Pythonic way to get backwards
backward=statement[::-1]
print("Komunikat wspak utworzony za pomocą wycinka [::-1]:",backward)

# Using 'for' loop and indexes
backward2=''
for i in range(-1,(-len(statement)-1),-1):
    backward2+=statement[i]
print("Komunikat wspak utworzony za pomocą ujemnych indeksów i pętli for:",backward2)

input()
