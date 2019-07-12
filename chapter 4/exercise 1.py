# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 4, exercise 1

print("Program odliczający kolejne liczby. \n")

start=int(input("Wprowadź liczbę początkową: "))
end=int(input("Wprowadź liczbę końcową: "))
step=int(input("Wprowadź krok: "))

print()

for i in range(start,end+1,step):
    print(i)

input()
