# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 9, exercise 2

class War_Card(object):
    """ """
    RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    SUITS = ['c','d','h','s']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.set_value()

    def __str__(self):
        return self.rank + self.suit

    def set_value(self):
        return self.RANKS.index(self.rank) + 2

class Player(object):
    """ Player's hand """
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = str(self.cards[0])
            return rep
        else:
            return 'pusta'

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def get_value(self):
        if self.cards:
            return self.cards[0].value

    def get_name(self):
        return self.name

class Deck(Player):
    """ """
    def populate(self):
        for rank in War_Card.RANKS:
            for suit in War_Card.SUITS:
                self.add(War_Card(rank, suit))

    def shuffle_cards(self):
        import random
        if self.cards:
            random.shuffle(self.cards)

    def give_card(self, hand):
        hand.add(self.cards[0])
        self.cards.remove(self.cards[0])


class Game(object):
    """ """
    def __init__(self, players):
        self.players = players

    def play(self):
        # creating deck
        war_deck = Deck('talia')
        war_deck.populate()
        war_deck.shuffle_cards()

        # giving card for each player
        for player in self.players:
            war_deck.give_card(player)

        # displaying card for each player
        for player in self.players:
            print(player.get_name() + ":")
            print(player)

        # setting winner
        if self.players[0].get_value() > self.players[1].get_value():
            print("\nZwycięzca: " + self.players[0].get_name())
        elif self.players[0].get_value() < self.players[1].get_value():
            print("\nZwycięzca: " + self.players[1].get_name())
        else:
            print("\nRemis ")

        # clearing hands
        for player in self.players:
            player.clear()

def main():
    print("""Witaj w grze karcianej W Wojnę. 
    
    0 - zakończ
    1 - graj z komputerem
    2 - dwóch graczy \n""")
    answer = input("Wybierasz: ")

    if answer == '1':
        name = input("Podaj swoje imię: ")
        players = [Player(name), Player('Komputer')]
        gra = Game(players)
        gra.play()
        
        again = 't'
        while again.lower() not in ('n', 'nie', 'no'):
            again = input("\nCzy chcesz zagrać ponownie? (t/n): ")
            if again.lower() in ('t', 'tak', 'y', 'yes'):
                gra.play()
                
    elif answer == '2':
        name1 = input("Podaj nazwę pierwszego gracza: ")
        name2 = input("Podak nazwę drugiego gracza: ")
        players = [Player(name1), Player(name2)]

        gra = Game(players)
        gra.play()

        again = 't'
        while again.lower() not in ('n', 'nie', 'no'):
            again = input("\nCzy chcesz zagrać ponownie? (t/n): ")
            if again.lower() in ('t', 'tak', 'y', 'yes'):
                gra.play()
        
    elif answer == '0':
        pass
        
    else:
        print("błędny wybór")

main()

input("\nAby zakończyć naciśnij klawisz ENTER ")
