# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 10, exercise 3
#
#===================================================================================================
# ADD MEALS HERE, as tuple:
# (<string>description, <int>price)

SNAPS = (('pieczywo czosnkowe 10zł', 10), ('krążki cebulowe 12zł', 12),
         ('paluszki chlebowe 12zł', 12))

SOUPS = (('rosół z torebki 5zł', 5), ('rosół z kury 15zł', 15),
         ('pomidorowa 18zł', 18), ('zupa z trupa 200zł', 200))

DINNERS = (('ryba z frytkami 25zł', 25), ('kotlet schabowy 30zł', 30),
           ('shoarma wieprzowa 35zł', 35), ('shoarma wołowa 40zł', 40),
           ('stek wołowy 50zł', 50), ('stek z antrykotu 70zł', 70),
           ('kaszka z betonu 101zł', 101), ('szarańcza w pomarańczach 1001zł', 1001),
           ('bigos sprzed tygodnia 10zł', 10), ('szprotki z puszki 8zł', 8))

DRINKS = (('woda święcona 500zł', 500), ('woda świecona 8zł', 8),
          ('pepsi-cola 10zł', 10), ('tanie wino 50zł', 50),
          ('jabol 150zł', 150))

DESSERTS = (('bajaderka 7,50zł', 7.5), ('ciastko z wróżbą 666zł', 666),
            ('sernik bez sera 18zł', 18))

#===================================================================================================
import tkinter as tk
from functools import partial
from tkinter import scrolledtext
from tkinter import font

# variable used as global in functions
bill_log = ''   # represents ordered meals on scrolledtext widget
bill_total = 0  # represents price for order

def add_to_bill(food):
    global bill_log
    entry = food[0] + '\n'
    bill_log += entry
    bill_scr_text.config(state=tk.NORMAL)
    bill_scr_text.delete(0.0, tk.END)
    bill_scr_text.insert(0.0, bill_log)
    bill_scr_text.config(state=tk.DISABLED)

    global bill_total
    bill_total += food[1]
    bill_lbl_count['text'] = 'Do zapłaty ' + str(bill_total)

    bttn_send['state']=tk.NORMAL

def clear_bill():
    """ Activate scrolledtext, clear, disable, reset bill_log & bill_total """
    bill_scr_text.config(state=tk.NORMAL)
    bill_scr_text.delete(0.0, tk.END)
    bill_scr_text.config(state=tk.DISABLED)
    global bill_log
    bill_log = ''
    global bill_total
    bill_total = 0
    bill_lbl_count['text'] = 'Do zapłaty 0,00zł'
    
    bttn_send['state']=tk.DISABLED

def order():
    from tkinter import messagebox
    messagebox.showinfo('Zamówienie złożone', 'Przyjęto zamówienie, ale nie rób sobie ' +
                        'nadziei, że ktokolwiek przyjedzie. ')

win = tk.Tk()
win.title('Złóż zamówienie!')
win.geometry('800x500')
win.resizable(width='FALSE', height='FALSE')

# set image for background
try:
    photo = tk.PhotoImage(file='exercise 3.png')
    label = tk.Label(win, image=photo)
    label.image = photo
    label.grid(row=0, column=0, columnspan=20, rowspan=20)
except:
    pass

# Fonts settings
logo_font = font.Font(win, family="Berlin Sans FB Demi", size=36)
frames_font = font.Font(win, family="Bahnschrift SemiLight", size=12, weight='bold')

# ALL WIDGETS BELOW:  
#===================================================================================================
# Upper Frame, logo Mamma Mia!
frame_0 = tk.Frame(win, width=800, height=100)
frame_0.grid(column=0, row=0, columnspan=4)

tk.Label(frame_0, text='Mamma Mia!', font=logo_font, width=28).grid(columnspan=4)

#============================================
# Left Frame, snaps and soups
frame_1 = tk.Frame(win, width=200, height=400)
frame_1.grid(column=0, row=1)

if SNAPS:
    snaps_frame = tk.LabelFrame(frame_1, text='Przystawki', font=frames_font)
    snaps_frame.grid(column=0, row=0)
    for i in range(len(SNAPS)):
        action = partial(add_to_bill, SNAPS[i])
        tk.Button(snaps_frame, text=SNAPS[i][0], width=20, wraplength=160, 
                  command=action).grid(column=0, row=i)

if SOUPS:
    soups_frame = tk.LabelFrame(frame_1, text='Zupy', font=frames_font)
    soups_frame.grid(column=0, row=1)
    for i in range(len(SOUPS)):
        action = partial(add_to_bill, SOUPS[i])
        tk.Button(soups_frame, text=SOUPS[i][0], width=20, wraplength=160, 
                  command=action).grid(column=0, row=i)
        
#============================================
# Middle Frame, dinners
frame_2 = tk.Frame(win, width=200, height=400)
frame_2.grid(column=1, row=1)

if DINNERS:
    dinners_frame = tk.LabelFrame(frame_2, text='Dania główne', font=frames_font)
    dinners_frame.grid(column=0, row=0)
    for i in range(len(DINNERS)):
        action = partial(add_to_bill, DINNERS[i])
        tk.Button(dinners_frame, text=DINNERS[i][0], width=20, wraplength=160, 
                  command=action).grid(column=0, row=i)

#============================================
# Right Frame, drinks and desserts
frame_3 = tk.Frame(win, width=200, height=400)
frame_3.grid(column=2, row=1)

if DRINKS:
    drinks_frame = tk.LabelFrame(frame_3, text='Napoje', font=frames_font)
    drinks_frame.grid(column=0, row=0)
    for i in range(len(DRINKS)):
        action = partial(add_to_bill, DRINKS[i])
        tk.Button(drinks_frame, text=DRINKS[i][0], width=20, wraplength=160, 
                  command=action).grid(column=0, row=i)

if DESSERTS:
    desserts_frame = tk.LabelFrame(frame_3, text='Desery', font=frames_font)
    desserts_frame.grid(column=0, row=1)
    for i in range(len(DESSERTS)):
        action = partial(add_to_bill, DESSERTS[i])
        tk.Button(desserts_frame, text=DESSERTS[i][0], width=20, wraplength=160, 
                  command=action).grid(column=0, row=i)

#============================================
# Bill Frame
frame_4 = tk.Frame(win, width=200, height=400)
frame_4.grid(column=3, row=1)

bill_scr_text = scrolledtext.ScrolledText(frame_4, width=25, height=18)
bill_scr_text.config(state=tk.DISABLED)
bill_scr_text.grid(column=0, row=0)

bill_lbl_count = tk.Label(frame_4, text='Do zapłaty 0,00zł')
bill_lbl_count.grid(column=0, row=1, sticky=tk.E)

bttn_cancel = tk.Button(frame_4, text='Wyczyść zamówienie', command=clear_bill)
bttn_cancel.grid(column=0, row=2, sticky=tk.E)

bttn_send = tk.Button(frame_4, text='Złóż zamówienie', command=order, height=2)
bttn_send['state']=tk.DISABLED
bttn_send.grid(column=0, row=3, sticky=tk.EW)


win.mainloop()
