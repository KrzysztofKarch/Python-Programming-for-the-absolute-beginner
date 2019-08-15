# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 10, exercise 1

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text='Program tworzący głupawą, choć prawdziwą historyjkę o Francuzach. \n',
              ).grid(row=0, column=0, columnspan=4, sticky=W)
        Label(self,
              text='Imię postaci '
              ).grid(row=2, column=0, sticky=W)
        # name
        self.name=Entry(self)
        self.name.focus()
        self.name.grid(row=2, column=1, sticky=W)
        # clothes
        Label(self,
              text='Ubranie ',
              ).grid(row=3, column=0, sticky=W)
        self.has_cloak=BooleanVar()
        Checkbutton(self,
                    text='płaszcz',
                    variable=self.has_cloak,
                    width='5',
                    ).grid(row=3, column=1, sticky=W)
        self.has_hat=BooleanVar()
        Checkbutton(self,
                    text='kapelusz',
                    variable=self.has_hat,
                    width='5',
                    ).grid(row=3, column=1, columnspan=2)
        self.has_beret=BooleanVar()
        Checkbutton(self,
                    text='beret',
                    variable=self.has_beret,
                    width='5',
                    ).grid(row=3, column=2)
        # activity
        Label(self,
              text='Ulubione zajęcie',
              ).grid(row=4, column=0, sticky=W)
        self.activity=Entry(self)
        self.activity.grid(row=4, column=1, sticky=W)
        # miss
        Label(self,
              text='Wybierz:',
              ).grid(row=5, column=0, sticky=W)
        self.miss=StringVar()
        self.miss.set(None)
        Radiobutton(self,
                    variable=self.miss,
                    text='uciekł',
                    value='uciekł',
                    ).grid(row=5, column=1, sticky=W)
        Radiobutton(self,
                variable=self.miss,
                text='przepadł',
                value='przepadł',
                ).grid(row=6, column=1, sticky=W)
        Radiobutton(self,
                    variable=self.miss,
                    text='zaginął',
                    value='zaginął',
                    ).grid(row=7, column=1, sticky=W)
        # create story button
        Button(self, text='Generuj', command=self.create_story
               ).grid(row=9, column=0, sticky=W)
        self.text=Text(self, width=61, height=8, wrap=WORD)
        self.text.grid(row=10, column=0, columnspan=4, sticky=W)

    def create_story(self):
        # get story info
        name=self.name.get()
        clothes=''
        if self.has_cloak.get():
            clothes+=' płaszcz,'
        if self.has_hat.get():
            clothes+=' kapelusz,'
        if self.has_beret.get():
            clothes+=' beret,'
                 
        # create story
        story='Był sobie mały Francuz imieniem '
        story+=name
        story+=' i miał na sobie kretyńskie pantofelki,'
        story+=clothes
        story+=' okulary. Jego ulubionymi zajęciami była ucieczka, '\
                'kolaboracja z Niemcami i francuskie pocałunki, a także '
        story+=self.activity.get()
        story+='. Niestety ów Francuzik '
        story+=self.miss.get()
        story+=' i nie było z niego żadnego pożytku. '


        # display story
        self.text.delete(0.0, END)
        self.text.insert(0.0, story)


# main
root = Tk()
root.geometry('500x350')
root.title('Mad Lib exercise 1')

app = Application(root)
root.mainloop()
