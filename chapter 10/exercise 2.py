# Notebook

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class Application(ttk.Notebook):
    def __init__(self, master):
        super(Application, self).__init__(master)
        # create 2 Notebook tabs
        self.tab1=Frame(self)
        self.tab2=Frame(self)
        self.add(self.tab1, text='Program')
        self.add(self.tab2, text='Log')
        self.pack(expand=1, fill='both')

        # create empty log at start
        self.log=''
    
        self.create_widgets_tab1()
        self.create_widgets_tab2()
        self.disable_widgets()

    # all widgets on tab1
    def create_widgets_tab1(self):
        Label(self.tab1, text='Odgadnij liczbę od 1 do 100\n').grid(row=0, column=0, columnspan=2, sticky=W)
        self.bttn_start=Button(self.tab1, text='Start', command=self.new_game)
        self.bttn_start.focus()
        self.bttn_start.grid(row=1, column=0, sticky=W)

        Label(self.tab1, text='Pozostało prób: ').grid(row=2, column=0, sticky=W)
        self.lbl_tries_left=Label(self.tab1, text='')
        self.lbl_tries_left.grid(row=2, column=1)
        
        Label(self.tab1, text='Zgaduję: ').grid(row=3, column=0, sticky=W)
        self.entry_guess=Entry(self.tab1)
        self.entry_guess.grid(row=3, column=1)
        
        self.bttn_guess=Button(self.tab1, text='zatwierdź', command=self.play)
        self.bttn_guess.grid(row=3, column=2, columnspan=3)

        self.result=Label(self.tab1, text='')
        self.result.grid(row=4, column=0, sticky=W)

    # all widgets on tab2
    def create_widgets_tab2(self):
        self.scrl_text = scrolledtext.ScrolledText(self.tab2, width=47, height=10)
        self.scrl_text.grid()

    # disable entry and button on first_run/win/loose
    def disable_widgets(self):
        self.entry_guess['state']='disabled'
        self.bttn_guess['state']='disabled'

    # start new game
    # create rundom number, set tries to 7, enable entry and button
    def new_game(self):
        import random
        self.number = random.randint(1, 100)
        self.tries_left=7
        
        # update screen
        self.lbl_tries_left.configure(text=7)
        self.result['text']=''
        self.entry_guess['state']='normal'
        self.entry_guess.delete(0, END)
        self.bttn_guess['state']='normal'

        # update log
        self.log+='wylosowano liczbę\n'
        self.display_log()

    # here the game is played
    def play(self):
        guess = self.entry_guess.get()

        # check guess for proper value and range
        try:
            guess=int(guess)
            if guess not in range(1, 101):
                raise ValueError

            # if guess has proper value, compare
            if guess > self.number:
                self.result['text']='za duża'
            elif guess < self.number:
                self.result['text']='za mała'
            elif guess == self.number:
                self.result['text']='Zgadłeś!'
                self.disable_widgets()

            # guess compared, so remove 1 try
            self.tries_left -= 1
            self.lbl_tries_left.configure(text=self.tries_left)

            # no tries left and no good guess on last one
            if self.tries_left == 0 and guess != self.number:
                self.result['text']='przegrałeś'
                self.disable_widgets()

            # update log
            self.log+='zgadujesz ' + str(guess) + '\n'
            self.display_log()

        # player wrote wrong value
        except ValueError:
            self.result['text']='błędna wartość'

    # show log on tab2
    def display_log(self):
        self.scrl_text.delete(0.0, END)
        self.scrl_text.insert(0.0, self.log)      
        
def main():
    root=Tk()
    root.geometry('400x200')
    root.title('Exercise 2')

    app=Application(root)
    root.mainloop()

main()
