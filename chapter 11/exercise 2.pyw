# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 11, exercise 2

from livewires import games
import random

games.init(screen_width=1070, screen_height=748, fps=50)

class Stone_thrower(games.Sprite):
    "Creates falling stones, made as Sprite object for build-in update() function"
    image=games.load_image("exercise 2 stone.jpg")

    def __init__(self, host):
        super(Stone_thrower, self).__init__(image=Stone_thrower.image, bottom=0)
        self.host = host #reference to Game object
        self.time_to_drop=120 #counter for throwing stones and balls

    def update(self):
        "counts down to throwing stones and balls"
        self.time_to_drop-=1
        #big stone
        if self.time_to_drop<=0:
            falling_stone=Stone(host=self.host, x=random.randrange(games.screen.width),
                dy=random.randrange(1,3))
            games.screen.add(falling_stone)
            self.time_to_drop=random.randrange(120,200) #reset counter
        #small stone
        if self.time_to_drop % 40 == 0:
            dx_speed=(-2,-1,1,2)
            falling_ball=Ball(host=self.host, x=random.randrange(0, 1070), dx=random.choice(dx_speed),
                dy=random.randrange(1,3))
            games.screen.add(falling_ball)

class Stone(games.Sprite):
    "Big falling stone"
    image=games.load_image("exercise 2 stone.jpg")

    def __init__(self, host, x, dy):
        super(Stone, self).__init__(image=Stone.image,
            x=x, bottom=0, dy=dy)
        self.host = host #reference to Game object

    def update(self):
        #if sprite is overlapping scoreboard, redraw it
        if self.right > 900 and self.top < 100:
            self.host.display_scoreboard()
        #if sprite is at the bottom add scores and destroy
        if self.bottom > games.screen.height:
            self.host.increase_score(10)
            self.destroy()

class Ball(games.Sprite):
    "Small circular falling stone"
    image=games.load_image("exercise 2 ball.bmp")

    def __init__(self, host, x, dx, dy):
        super(Ball, self).__init__(image=Ball.image,
            x=x, dx=dx, bottom=0, dy=dy)
        self.host = host #reference to Game object

    def update(self):
        #if sprite is overlapping scoreboard, redraw it
        if self.right > 900 and self.top < 100:
            self.host.display_scoreboard()
        #if sprite is at the bottom add scores and destroy
        if self.bottom > games.screen.height:
            self.host.increase_score(2)
            self.destroy()

class Player(games.Sprite):
    "Represents player object with his moves and life/stamina attributes "
    image=games.load_image("exercise 2 horse right.bmp")

    def __init__(self, host):
        super(Player, self).__init__(image=Player.image,
        x=games.mouse.x, bottom=games.screen.height, interval=games.screen.fps)
        self.host = host
        self.stamina = 100
        self.life = 100

        self.stamina_bar = games.Text(value = "Stamina - " + str(self.stamina),
            size = 40, color = (0, 100, 0), top = 15, left = 15)
        games.screen.add(self.stamina_bar)
        self.life_bar = games.Text(value = "Life - " + str(self.life),
            size = 40, color = (200, 0, 0), top = 55, left = 15)
        games.screen.add(self.life_bar)

    def update(self):
        # moving right and left
        if self.x < games.mouse.x:
            self.x+=2
            right_image=games.load_image("exercise 2 horse right.bmp")
            self.image=self.set_image(right_image)
        if self.x > games.mouse.x:
            self.x-=2
            left_image=games.load_image("exercise 2 horse left.bmp")
            self.image=self.set_image(left_image)
        # fast moving, consumes stamina
        if self.x < games.mouse.x and games.mouse.is_pressed(0) and self.stamina > 0:
            self.x+=4
            self.stamina -= 1
            self.update_stamina_bar()
        if self.x > games.mouse.x and games.mouse.is_pressed(0) and self.stamina > 0:
            self.x-=4
            self.stamina -= 1
            self.update_stamina_bar()

        # improve display at the edges
        if self.left<0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width

        self.check_collision()

        # make sure stamina_bar and life_bar is on top of other sprites
        if self.stamina_bar.overlaps:
            self.update_stamina_bar()
        if self.life_bar.overlaps:
            self.update_life_bar()

    def check_collision(self):
        "removes player's life"
        for thing in self.overlapping_sprites:
            # big hitting Stone
            if isinstance(thing, Stone):
                self.life -= 51
                self.update_life_bar()
                thing.destroy()
            # averge hitting Ball
            if isinstance(thing, Ball):
                self.life -= 34
                self.update_life_bar()
                thing.destroy()
        # player is dead
        if self.life <= 0:
            self.life = 0
            self.host.end_game()
            self.destroy()

    def update_stamina_bar(self):
        "redrawing stamina_bar"
        self.stamina_bar.destroy()
        self.stamina_bar = games.Text(value = "Stamina - " + str(self.stamina),
            size = 40, color = (0, 100, 0), top = 15, left = 15)
        games.screen.add(self.stamina_bar)

    def update_life_bar(self):
        "redrawing life_bar"
        self.life_bar.destroy()
        self.life_bar = games.Text(value = "Life - " + str(self.life),
            size = 40, color = (200, 0, 0), top = 55, left = 15)
        games.screen.add(self.life_bar)

    def tick(self):
        "Regeneration"
        if self.stamina < 100:
            self.stamina += 1
            self.update_stamina_bar()
        if self.life < 100:
            self.life += 1
            self.update_life_bar()

class Game(object):
    "represents game object with creating new game, score, play, end"
    def __init__(self):
        self.score = 0
        self.scoreboard = games.Text(value = 0, size = 40, color = (0, 0, 0),
            top = 15, right = games.screen.width - 15)
        games.screen.add(self.scoreboard)
        self.is_playing = True

        tip = games.Message(value = "Hold LMB for fast moving",
            size = 50, color = (200, 0, 0), x = games.screen.width/2, y = games.screen.height/2,
            lifetime = 5 * games.screen.fps)
        games.screen.add(tip)

    def play(self):
        player=Player(self)
        games.screen.add(player)

        thrower=Stone_thrower(self)
        games.screen.add(thrower)

    def increase_score(self, points):
        if self.is_playing:
            self.score += points
            self.display_scoreboard()

    def display_scoreboard(self):
        "redrawing scoreboard"
        self.scoreboard.destroy()
        self.scoreboard = games.Text(value = self.score, size = 40, color = (0, 0, 0),
            top = 15, right = games.screen.width - 15)
        games.screen.add(self.scoreboard)

    def end_game(self):
        "stops increasing score, closes the window after delay"
        self.is_playing = False
        message = "Koniec gry. Wynik " + str(self.score)
        end = games.Message(value = message,
            size = 90,
            color = (200, 0, 0),
            x = games.screen.width/2,
            y = games.screen.height/2,
            lifetime = 5 * games.screen.fps,
            after_death = games.screen.quit)
        games.screen.add(end)

def main():
    background=games.load_image("exercise 2 background.jpg", transparent=False)
    games.screen.background=background

    game=Game()
    game.play()

    games.screen.mainloop()

if __name__=="__main__":
    main()
