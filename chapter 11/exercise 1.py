# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 11, exercise 1
#
# Pizza Panic
# Gracz musi złapać lecące w dół pizze, zanim spadną na ziemię

from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    """
    Patelnia sterowana przez gracza służąca do łapania spadających pizz.
    """
    image = games.load_image("exercise 1 pan.bmp")

    def __init__(self, my_chef):
        """ Initialize Pan object and create Text object for score. """
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        self.my_chef = my_chef      
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        """ Sprawdź, czy nie zostały złapane jakieś pizze. """
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10 
            pizza.handle_caught()

            # increasing difficulty by adding second Chef and leveling them up
            if int(self.score.value) == 100:
                self.my_chef.level_up()
            if int(self.score.value) == 200:
                self.new_chef = Chef()
                games.screen.add(self.new_chef)
            if int(self.score.value) == 500:
                self.my_chef.level_up()
                self.new_chef.level_up()

class Pizza(games.Sprite):
    """
    Pizza, która spada na ziemię.
    """ 
    image = games.load_image("exercise 1 pizza.bmp")  

    def __init__(self, x, y = 90, dy = 1):  # modyfication allows set 'dy' speed
        """ Inicjalizuj obiekt klasy Pizza. """
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = dy)

    def update(self):
        """ Sprawdź, czy dolny brzeg pizzy dosięgnął dołu ekranu. """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Destroy self if caught. """
        self.destroy()

    def end_game(self):
        """ Zakończ grę. """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    """
    Szef kuchni, który porusza się w lewo i w prawo, zrzucając pizze.
    """
    image = games.load_image("exercise 1 chef.bmp")

    def __init__(self, y = 55, dx = 2, odds_change = 300):
        """ Initialize the Chef object. """
        super(Chef, self).__init__(image = Chef.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = dx)
        
        self.odds_change = odds_change
        self.time_til_drop = 0
        self.throwing_speed = 2     # used as argument for 'dy' in Pizza object creation

    def update(self):
        """ Ustal, czy kierunek ruchu musi zostać zmieniony na przeciwny. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
                
        self.check_drop()

    def check_drop(self):
        """ Zmniejsz licznik odliczający czas lub zrzuć pizzę i zresetuj odliczanie. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x, dy = self.throwing_speed)
            games.screen.add(new_pizza)

            # ustaw margines na mniej więcej 30% wysokości pizzy, niezależnie od prędkości pizzy   
            self.time_til_drop = int(new_pizza.height * 1.3) + 1

    def level_up(self):
        """ Increasing difficulty """
        level_up_msg = games.Message(value = "Level up!",
                                    size = 60,
                                    color = color.black,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 1.5 * games.screen.fps)
        games.screen.add(level_up_msg)
        
        self.time_til_drop = 100 + random.randrange(1, 50)    # 2-3s pause in throwing pizzas

        # increase Chef moving speed
        if self.dx > 0:
            self.dx += 1
        else:
            self.dx -= 1

        # increase pizza 'dy' speed
        self.throwing_speed += 1

def main():
    """ Uruchom grę. """
    wall_image = games.load_image("exercise 1 wall.jpg", transparent = False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    # Pan object need to has reference to Chef to be allowed to increase difficulty
    the_pan = Pan(my_chef = the_chef)   
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = True
    
    games.screen.mainloop()

# wystartuj!
main()
