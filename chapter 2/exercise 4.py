# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 2, exercise 4

print("Program to calculate total price of a car. ")
price = int(input("Enter car price: "))

print("""\nCharges: 
Vat tax, +22%
Registration fee, +5%
Dealer commision, +1000
Transportation fee, +500""")

price_total = price * 1.22 * 1.05 + 1000 + 500

print("\n\nTotal price:", price_total)
input("\n\nPress Enter to exit. ")
