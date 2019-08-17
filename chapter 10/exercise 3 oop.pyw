# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 10, exercise 3

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()

        self.bill_log = ''      # represents ordered meals
        self.bill_total = 0     # represents price for order

        # ADD MEALS HERE, as tuple
        # (<string>description, <int>price)
        self.SNAPS = (('pieczywo czosnkowe 10zł', 10), ('krążki cebulowe 12zł', 12),
                      ('paluszki chlebowe 12zł', 12))

        self.SOUPS = (('rosół z torebki 5zł', 5), ('rosół z kury 15zł', 15),
                      ('pomidorowa 18zł', 18), ('zupa z trupa 200zł', 200))

        self.DINNERS = (('ryba z frytkami 25zł', 25), ('kotlet schabowy 30zł', 30),
                        ('shoarma wieprzowa 35zł', 35), ('shoarma wołowa 40zł', 40),
                        ('stek wołowy 50zł', 50), ('stek z antrykotu 70zł', 70),
                        ('kaszka z betonu 101zł', 101), ('szarańcza w pomarańczach 1001zł', 1001),
                        ('bigos sprzed tygodnia 10zł', 10), ('szprotki z puszki 8zł', 8))

        self.DRINKS = (('woda święcona 500zł', 500), ('woda świecona 8zł', 8),
                       ('pepsi-cola 10zł', 10), ('tanie wino 50zł', 50),
                       ('jabol 150zł', 150))

        self.DESSERTS = (('bajaderka 7,50zł', 7.5), ('ciastko z wróżbą 666zł', 666),
                         ('sernik bez sera 18zł', 18))

        self.load_background()  # load restaurant image
        self.set_fonts()        # set fonts for LabelFrames
        self.create_widgets()   # create 5 Frames, all buttons

    def add_to_bill(self, food):
        # update bill_log (listed food names) by making it available, clear, add new value,
        # then disable to edit
        self.bill_log += food[0] + '\n'
        self.bill_scr_text['state']=tk.NORMAL
        self.bill_scr_text.delete(0.0, tk.END)
        self.bill_scr_text.insert(0.0, self.bill_log)
        self.bill_scr_text['state']=tk.DISABLED

        # update bill_total (price to pay)
        self.bill_total += food[1]
        self.bill_lbl_count['text']='Do zapłaty ' + str(self.bill_total)

        # activate order button
        self.bttn_send['state']=tk.NORMAL

    def clear_bill(self):
        """ Remove all meals from order """
        """ Activate scrolledtext, clear it, then disable, reset bill_log & bill_total """
        self.bill_scr_text['state']=tk.NORMAL
        self.bill_scr_text.delete(0.0, tk.END)
        self.bill_scr_text['state']=tk.DISABLED

        self.bill_log = ''
        self.bill_total = 0
        self.bill_lbl_count['text']='Do zapłaty 0,00zł'

        # deactivate order button (because order is empty)
        self.bttn_send['state']=tk.DISABLED

    def order(self):
        from tkinter import messagebox
        messagebox.showinfo('Zamówienie złożone', 'Przyjęto zamówienie, ale nie rób sobie ' +
                            'nadziei, że ktokolwiek przyjedzie. ')

    def load_background(self):
        try:
            photo = tk.PhotoImage(file='exercise 3.png')
            label = tk.Label(self, image=photo)
            label.image = photo
            label.grid(row=0, column=0, columnspan=20, rowspan=20)
        except:
            pass

    def set_fonts(self):
        from tkinter import font
        self.logo_font = font.Font(self, family="Berlin Sans FB Demi", size=36)
        self.frames_font = font.Font(self, family="Bahnschrift SemiLight", size=12, weight='bold')

    def create_widgets(self):
        """ Creates all widgets. 5 Frames: 1 - horizontal with logo, 4 - vertical. """
        from functools import partial
        from tkinter import scrolledtext

        # Upper Frame, logo Mamma Mia!
        self.frame_0 = tk.Frame(self, width=800, height=100)
        self.frame_0.grid(column=0, row=0, columnspan=4)

        tk.Label(self.frame_0, text='Mamma Mia!', font=self.logo_font, width=28).grid(columnspan=4)

        # Left Frame, snaps and soups
        self.frame_1 = tk.Frame(self, width=200, height=400)
        self.frame_1.grid(column=0, row=1)

        if self.SNAPS:
            self.snaps_frame = tk.LabelFrame(self.frame_1, text='Przystawki', font=self.frames_font)
            self.snaps_frame.grid(column=0, row=0)
            for i, elem in enumerate(self.SNAPS):
                action = partial(self.add_to_bill, elem)
                tk.Button(self.snaps_frame, text=elem[0], width=20, wraplength=160,
                          command=action).grid(column=0, row=i)

        if self.SOUPS:
            self.soups_frame = tk.LabelFrame(self.frame_1, text='Zupy', font=self.frames_font)
            self.soups_frame.grid(column=0, row=1)
            for i, elem in enumerate(self.SOUPS):
                action = partial(self.add_to_bill, elem)
                tk.Button(self.soups_frame, text=elem[0], width=20, wraplength=160,
                          command=action).grid(column=0, row=i)

        # Middle Frame, dinners
        self.frame_2 = tk.Frame(self, width=200, height=400)
        self.frame_2.grid(column=1, row=1)

        if self.DINNERS:
            self.dinners_frame = tk.LabelFrame(self.frame_2, text='Dania główne', font=self.frames_font)
            self.dinners_frame.grid(column=0, row=0)
            for i, elem in enumerate(self.DINNERS):
                action = partial(self.add_to_bill, elem)
                tk.Button(self.dinners_frame, text=elem[0], width=20, wraplength=160,
                          command=action).grid(column=0, row=i)

        # Right Frame, drinks and desserts
        self.frame_3 = tk.Frame(self, width=200, height=400)
        self.frame_3.grid(column=2, row=1)

        if self.DRINKS:
            self.drinks_frame = tk.LabelFrame(self.frame_3, text='Napoje', font=self.frames_font)
            self.drinks_frame.grid(column=0, row=0)
            for i, elem in enumerate(self.DRINKS):
                action = partial(self.add_to_bill, elem)
                tk.Button(self.drinks_frame, text=elem[0], width=20, wraplength=160,
                          command=action).grid(column=0, row=i)

        if self.DESSERTS:
            self.desserts_frame = tk.LabelFrame(self.frame_3, text='Desery', font=self.frames_font)
            self.desserts_frame.grid(column=0, row=1)
            for i, elem in enumerate(self.DESSERTS):
                action = partial(self.add_to_bill, elem)
                tk.Button(self.desserts_frame, text=elem[0], width=20, wraplength=160,
                          command=action).grid(column=0, row=i)

        # Bill Frame
        self.frame_4 = tk.Frame(self, width=200, height=400)
        self.frame_4.grid(column=3, row=1)

        self.bill_scr_text = scrolledtext.ScrolledText(self.frame_4, width=25, height=18)
        self.bill_scr_text.config(state=tk.DISABLED)
        self.bill_scr_text.grid(column=0, row=0)

        self.bill_lbl_count = tk.Label(self.frame_4, text='Do zapłaty 0,00zł')
        self.bill_lbl_count.grid(column=0, row=1, sticky=tk.E)

        self.bttn_cancel = tk.Button(self.frame_4, text='Wyczyść zamówienie', command=self.clear_bill)
        self.bttn_cancel.grid(column=0, row=2, sticky=tk.E)

        self.bttn_send = tk.Button(self.frame_4, text='Złóż zamówienie', command=self.order, height=2)
        self.bttn_send['state']=tk.DISABLED
        self.bttn_send.grid(column=0, row=3, sticky=tk.EW)

def main():
    win = tk.Tk()
    win.geometry('800x500')
    win.title('Złóż zamówienie')
    win.resizable(width='FALSE', height='FALSE')

    app = App(win)

    win.mainloop()

if __name__ == '__main__':
    main()
