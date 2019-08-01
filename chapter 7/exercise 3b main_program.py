# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 7, exercise 3
#
# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys

def open_file(file_name, mode):
    """Otwórz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "Program zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    points = next_line(the_file)
    if points:
        points = int(points[0])
        
    explanation = next_line(the_file) 

    return category, question, answers, points, correct, explanation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def get_scoreboard(file):
    """Open file with scoreboard, create list of lines, edit each line and
        make scoreboard, then close the file."""
    scoreboard_file = open_file(file, "r")
    lines = scoreboard_file.readlines()
    scoreboard = []
    while lines:
        points = lines[0]
        points = points.replace("\n", "")
        points = int(points)
        name = lines[1]
        name = name.replace("\n", "")
        scoreboard.append((points, name))
        lines = lines[2:]
    scoreboard_file.close()
    return scoreboard

def show_scoreboard(scoreboard):
    print("\nLista najlepszych wyników: ")
    for i in scoreboard:
        print("%-30s" % i[1], "%3s" % i[0])

def update_scoreboard(scoreboard, score, file, number_of_scores = 3):
    """Take name of player and create file with new scoreboard.
        By default it saves only top 3 result.
        Return True if operation of updating was successful. """
    updated = False
    name = input("\nGratulacje możesz wpisać się na tablicę. Podaj swoją nazwę (ENTER - pomiń): ")
    if name:
        scoreboard.append((score, name))
        scoreboard.sort(reverse = True)
        
        new_scoreboard = []
        for i in range(number_of_scores):
            new_scoreboard.append(scoreboard[i])

        scoreboard_file = open_file(file, "w")
        for i in new_scoreboard:
            score = str(i[0])
            scoreboard_file.write(score)
            scoreboard_file.write("\n")
            name = i[1]
            scoreboard_file.write(name)
            scoreboard_file.write("\n")            
        scoreboard_file.close()
        updated = True
    return updated

def main():
    trivia_file = open_file("exercise 3 quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = int(0)

    # pobierz pierwszy blok
    category, question, answers, points, correct, explanation = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedź
        answer = input("Jaka jest Twoja odpowiedź?: ")

        # sprawdź odpowiedź
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += points
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, points, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)

    scoreboard = get_scoreboard("exercise 3 top_scores.txt")
    show_scoreboard(scoreboard)

    if score > scoreboard[-1][0]:
        new_score = update_scoreboard(scoreboard, score, "exercise 3 top_scores.txt")
        if new_score:
            scoreboard = get_scoreboard("exercise 3 top_scores.txt")
            show_scoreboard(scoreboard)
 
main()  
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
