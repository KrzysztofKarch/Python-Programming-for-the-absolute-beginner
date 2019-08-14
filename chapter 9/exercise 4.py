# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 9, exercise 3

import random

class Player(object):
    def __init__(self, name, life = 100, account = 0):
        self.name = name
        self.life = life
        self.account = account
        self.maps = []
        self.localization = None # not initialized 

    def __str__(self):
        rep = 'Obiekt klasy Player \n'
        rep += 'Name: ' + self.name + '\n'
        rep += 'Life: ' + str(self.life) + '\n'
        rep += 'Account: ' + str(self.account) + '\n'
        if self.localization:
            rep += 'Localization: ' + self.localization.get_name()
        else:
            rep += 'Localization: ' + 'not_initialized'
        return rep

    def set_home(self):
        self.localization = self.maps[0]

    def set_maps(self, maps):
        self.maps = maps

    def loose_life(self, damage):
        self.life -= damage
        if self.life > 0:
            print('\nPogonili Cię z widłami, zostajesz ranny')
        else:
            self.life = 0
            print('\nZabili Cię, w końcu musiało się to stać. \n')

    def heal(self):
        if self.account >= 20:
            self.account -= 20
            self.life += 50
            if self.life > 100:
                self.life = 100
            print('\nZostałeś uleczony')
        else:
            print('\nNie masz dość pieniędzy. ')

    def earn_money(self, amount):
        self.account += amount
        print('\nPobrano ' + str(amount) + '$ podatku')

    def demand_tax(self):
        self.localization.pay_or_fight(self)

    def show_info(self):
        print('Życie: ' + str(self.life))
        print('Konto: ' + str(self.account))
        print('Bieżąca lokalizacja: ' + self.localization.get_name())

    def travel(self):
        # display available localizations
        print()
        for index in range(len(self.maps)):
            print(str(index) + ' - ' + self.maps[index].get_name())

        # take player answer
        place_to_go = input('\nGdzie chcesz się udać? [0-' +str(len(self.maps) - 1) + ']: ')

        # check player answer for correct value
        try:
            place_to_go = int(place_to_go)
            if place_to_go in range(len(self.maps)):
                # change localization
                self.localization = self.maps[place_to_go]
                print('\nWyruszono do ' + self.localization.get_name())
            else:
                raise ValueError
        except ValueError:
            print('\nbłędna wartość')

    def get_life(self):
        return self.life

class City(object):
    def __init__(self, name, tax, aggression):
        self.name = name
        self.tax = tax
        self.aggression = aggression

    def __str__(self):
        rep = 'Obiekt klasy City \n'
        rep += 'Name: ' + self.name + '\n'
        rep += 'Tax: ' + str(self.tax) + '\n'
        rep += 'Aggression: ' + str(self.aggression)
        return rep

    def pay_or_fight(self, player):
        """ decide to pay to player or fight with player """
        if random.random() > self.aggression:
            self.pay(player)
        else:
            self.fight(player)

    def pay(self, player):
        """ pay and call increase_aggression """
        player.earn_money(self.tax)
        self.increase_aggression()

    def fight(self, player):
        """ deal damage to player and call decrease_aggression """
        player.loose_life(random.randint(1,50))
        self.decrease_aggression()

    def increase_aggression(self):
        self.aggression *= 1.5
        if self.aggression > 1:
            self.aggression = 0.9

    def decrease_aggression(self):
        self.aggression *= 0.66

    def get_name(self):
        return self.name

class Home(City):
    def __init__(self, name):
        super(City, self).__init__()
        self.name = name

    def __str__(self):
        rep = 'Obiekt klasy Home \n'
        rep += 'Name: ' + self.name + '\n'
        return rep

    def pay_or_fight(self, player):
        print('\nNie możesz żądać podatku od swojego domu. ')


class Game(object):
    def __init__(self):
        # create player and cities
        self.player = Player('default')
        self.cities = [Home('Dom'),
                       City('Wrocław', tax = random.randint(1, 15), aggression = random.random()),
                       City('Kraków', tax = random.randint(1, 15), aggression = random.random()),
                       City('Warszawa', tax = random.randint(1, 15), aggression = random.random()),
                       City('Łódź', tax = random.randint(1, 15), aggression = random.random()),
                       City('Sosnowiec', tax = random.randint(1, 15), aggression = random.random())]
        # give player the cities
        self.player.set_maps(self.cities)
        self.player.set_home()

        self.show_intro()

    def show_intro(self):
        print("""
    _______            _____      _ _           _             
   |__   __|          / ____|    | | |         | |            
      | | __ ___  __ | |     ___ | | | ___  ___| |_ ___  _ __ 
      | |/ _` \ \/ / | |    / _ \| | |/ _ \/ __| __/ _ \| '__|
      | | (_| |>  <  | |___| (_) | | |  __/ (__| || (_) | |   
      |_|\__,_/_/\_\  \_____\___/|_|_|\___|\___|\__\___/|_| """)
        print('\nWitaj w grze Poborca Podatkowy, Twoim zadaniem będzie podróżowanie \n'\
              'miedzy miastami i pobieranie podatku. Czeka Cie niełatwe zadanie - \n'\
              'strzeż się żądnych Twojej krwi obywateli. Pamiętaj, że zawsze możesz \n'\
              'schować się w domu i nigdy z niego nie wychodzić. \n')

    def show_menu(self):
        print("""
    1 - pobież podatek
    2 - podróżuj
    3 - kup apteczkę
    4 - zakończ \n""")

    def play(self):
        answer = ''
        while answer != '4':

            if self.player.get_life() > 0:
                self.show_menu()
                self.player.show_info()
                
                choice = input('Wybierasz: ')
                if choice == '1':
                    self.player.demand_tax()
                elif choice == '2':
                    self.player.travel()
                elif choice == '3':
                    self.player.heal()
                elif choice == '4':
                    answer = '4'
                else:
                    print('\nbłędna wartość') 
            else:
                self.player.show_info()
                print('\nKoniec gry. ')
                answer = '4'
            
# main
gra = Game()
gra.play()
