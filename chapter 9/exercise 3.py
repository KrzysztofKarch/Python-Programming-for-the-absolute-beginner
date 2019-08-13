# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 9, exercise 3
#
# Blackjack
# Od 1 do 7 graczy współzawodniczy z rozdającym

import karty, gry     

class BJ_Card(karty.Card):
    """ Karta do blackjacka. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(karty.Deck):
    """ Talia kart do blackjacka. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))

    # new method to check cards amount (exercise 1)
    def get_cards_amount(self):
        return len(self.cards)
    

class BJ_Hand(karty.Hand):
    """ Ręka w blackjacku. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # jeśli karta w ręce ma wartość None, to i wartość sumy wynosi None
        for card in self.cards:
            if not card.value:
                return None
        
        # zsumuj wartości kart, traktuj każdego asa jako 1
        t = 0
        for card in self.cards:
              t += card.value

        # ustal, czy ręka zawiera asa
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # jeśli ręka zawiera asa, a suma jest wystarczająco niska,
        # potraktuj asa jako 11
        if contains_ace and t <= 11:
            # dodaj tylko 10, ponieważ już dodaliśmy 1 za asa
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ Gracz w blackjacku. """
    # new constructor and 2 attributes for playing for cash (exercise 3)
    def __init__(self, name, account = 1000, bet = 0):
        super(BJ_Player, self).__init__(name)
        self.account = account
        self.bet = bet
    
    def is_hitting(self):
        response = gry.ask_yes_no("\n" + self.name + ", chcesz dobrać kartę? (T/N): ")
        return response == "t"

    def bust(self):
        print(self.name, "ma furę.")
        self.lose()

    # all bellow methods in BJ_Player modified for playing for cash (exercise 3)
    def lose(self):
        print(self.name, "przegrywa.")
        self.account -= self.bet
        self.clear_bet()

    def win(self):
        print(self.name, "wygrywa.")
        self.account += self.bet
        self.clear_bet()

    def push(self):
        print(self.name, "remisuje.")
        self.clear_bet()

    def set_bet(self):
        right_bet = False
        while not right_bet:
            bet = gry.ask_number("Za ile zagrasz? " + self.name + " (10-1000): ", low = 10, high = 1001)
            if bet <= self.account:
                right_bet = True
        self.bet = bet

    def clear_bet(self):
        self.bet = 0

    def display_account(self):
        print(self.name + " (" + str(self.account) + "$)")

    def is_bankrupt(self):
        return self.account < 10

    def get_name(self):
        return self.name
        
class BJ_Dealer(BJ_Hand):
    """ Rozdający w blackjacku. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ Gra w blackjacka. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Rozdający")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
           
    def play(self):
        self.show_accounts()
        
        # new method asking players for bets (exercise 3)
        for player in self.players:
            player.set_bet()
        
        # rozdaj każdemu początkowe dwie karty
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # ukryj pierwszą kartę rozdającego
        for player in self.players:
            print(player)
        print(self.dealer)

        # rozdaj graczom dodatkowe karty
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # odsłoń pierwszą kartę rozdającego 

        if not self.still_playing:
            # ponieważ wszyscy gracze dostali furę, pokaż tylko rękę rozdającego
            print(self.dealer)
        else:
            # daj dodatkowe karty rozdającemu
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # wygrywa każdy, kto jeszcze pozostaje w grze
                for player in self.still_playing:
                    player.win()                    
            else:
                # porównaj punkty każdego gracza pozostającego w grze z punktami rozdającego
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # usuń karty wszystkich graczy
        for player in self.players:
            player.clear()
        self.dealer.clear()

        # show accounts (exercise 3)
        self.show_accounts()

        # kick bankrupt (exercise 3)
        self.remove_bankrupt()

    # new method to fill cards amount if needed (exercise 1)
    def fill_cards(self):
        cards_in_deck = self.deck.get_cards_amount()
        if cards_in_deck < len(self.players) * 5 + 5:
            self.deck.populate()
            self.deck.shuffle()
            print("uzupełniono karty - wtasowano nową talię")

    # new method for displaying player's accounts (exercise 3)
    def show_accounts(self):
        print("Stan kont graczy: ")
        for player in self.players:
            player.display_account()
        print()

    # new, cruel method for removing players with not enough money to continue playing (exercise 3)
    def remove_bankrupt(self):
        for player in list(self.players):
            if player.is_bankrupt():
                self.players.remove(player)
                print("Gracz " + player.get_name() + " nie ma dość pieniędzy dla dalszej gry. ")
                print("Opuszcza grę. ")

    # returns players list (exercise 3)
    def get_players(self):
        return self.players

def main():
    print("\t\tWitaj w grze 'Blackjack'!\n")
    
    names = []
    number = gry.ask_number("Podaj liczbę graczy (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Wprowadź nazwę " + str(i+1) + ". gracza: ")
        while not name:
            print("błąd, nie wpowadzono nazwy gracza")
            name = input("Wprowadź nazwę " + str(i+1) + ". gracza: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)

    # because low money mean that players can be kick from game, main function was rebuilt too (exercise 3)
    game.play()

    again = None
    while again != "n":
        # checking if there are any players left (exercise 3)
        if game.get_players():
            again = gry.ask_yes_no("\nCzy chcesz zagrać ponownie? (T/N): ")
            # new method to fill cards amount if needed (exercise 1)
            game.fill_cards()
            game.play()
        else:
            print("\nWszyscy gracze odpadli. " )
            again = "n"


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



