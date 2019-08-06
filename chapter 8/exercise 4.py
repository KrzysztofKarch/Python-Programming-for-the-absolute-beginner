# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 8, exercise 4
#
# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

from random import randrange as rand

class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
    
    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Mniam, mniam.  Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    criters = []
    crit_amout = int(input("Ile chcesz mieć zwierzaków na farmie? "))
    for i in range(crit_amout):
        criters.append(Critter('noname', rand(10), rand(10)))

    choice = None  
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka
    
        0 - zakończ
        1 - słuchaj swoich zwierzaków
        2 - nakarm swoje zwierzaki
        3 - pobaw się ze swoimi zwierzakami
        """)
    
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli 
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            for i in criters:
                i.talk()
        
        # nakarm swojego zwierzaka
        elif choice == "2":
            for i in criters:
                i.eat()
         
        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            for i in criters:
                i.play()

        # nieznany wybór 
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
