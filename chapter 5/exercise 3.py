# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 5, exercise 3

family={'Michael Douglas':'Kirk Douglas',
          'Maciej Stuhr':'Jerzy Stuhr',
          'Angelina Jolie':'Jon Voight',
          'Charlie Sheen':'Martin Sheen',
          'Kate Hudson':'Kurt Russel'}

choice=None
while choice!='6':
    print("*************************")
    print("*  Kto jest Twoim tatą  *")
    print("*************************\n")

    print("1 - wyświetl cały słownik")
    print("2 - znajdź ojca")
    print("3 - dodaj parę syn-ojciec")
    print("4 - zmień ojca")
    print("5 - usuń parę")
    print("6 - zakończ\n")

    choice=input("Wybierasz: ")

    if choice=='1':
        print()
        print("%-20s" % "Syn:", "%-20s" % "Ojciec:")
        for son in family:     
            print("%-20s" % son, "%-20s" % family[son])
        input("\nWciśnij ENTER aby kontynuować...\n")

    elif choice=='2':
        find=input("Wpisz Imię Nazwisko: ")
        if find in family:
            print("\nOjciec: ")
            print(family[find])
        else:
            print("\nBrak informacji o takiej osobie. ")
        input("\nWciśnij ENTER aby kontynuować...\n")

    elif choice=='3':
        son=input("Wpisz Imię Nazwisko dziecka: ")
        if son in family:
            print("Ta osoba posiada już wpis, usuń lub zmodyfikuj go. ")
        else:
            father=input("Wpisz Imię Nazwisko ojca: ")
            family[son]=father
            print("Dodano wpis. ")
        input("\nWciśnij ENTER aby kontynuować...\n")
            
    elif choice=='4':
        son=input("Wpisz Imię Nazwisko dziecka: ")
        if son in family:
            father=input("Wpisz nowe Imię Nazwisko ojca: ")
            family[son]=father
            print("Zmodyfikowano wpis. ")
        else:
            print("Brak takiej osoby w słowniku. ")
        input("\nWciśnij ENTER aby kontynuować...\n")
        
    elif choice=='5':
        son=input("Wpisz Imię Nazwisko dziecka: ")
        if son in family:
            del family[son]
            print("Usunięto wpis. ")
        else:
            print("Brak takiej osoby w słowniku. ")
        input("\nWciśnij ENTER aby kontynuować...\n")

        
