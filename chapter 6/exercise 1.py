# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 6, exercise 1

def ask_number_step(question, low, high, step=1):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

number = ask_number_step("Podaj liczbę parzystą, 0 - 100: ", 0, 100, 2)
if number:
    print("Dziękuje. ")
input()
