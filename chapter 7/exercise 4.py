# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 7, exercise 4

import sys

def open_file(file, mode = "r"):
    try:
        f = open(file, mode)
    except IOError:
        print("Błąd otwarcia pliku", file)
        input("\nNaciśnij ENTER aby zakończyć program. ")
        sys.exit()
    else:
        return f

def get_block(file):
    category = file.readline()
    question = file.readline()
    question = question.replace("/", "\n")
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correct = file.readline().replace("\n", "")
    return category, question, answers, correct

def main():
    quiz_file = open_file("exercise 4 quiz.txt", "r")
    score = int(0)
    questions = int(0)
    category, question, answers, correct = get_block(quiz_file)

    print("Witaj w quizie o obsłudze plików i wyjątków w Pythonie! \n")
    while category:
        print(category)
        print(question)
        for i in answers:
            print(i)

        answer = input("Wybieram odpowiedź nr: ")
        if answer == correct:
            print("Odpowiedź prawidłowa. \n\n")
            score += 1
        else:
            print("Błędna odpowiedź. Poprawna odpowiedź to:", answers[int(correct) - 1], "\n")

        questions += 1
        category, question, answers, correct = get_block(quiz_file)

    result = score/questions * 100
    print("\nWynik:", "%.0f" % result, "%")

main()
input("\nNaciśnij ENTER aby zakończyć program. ")
