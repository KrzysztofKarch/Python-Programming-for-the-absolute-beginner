# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 8, exercise 2
#
# ASCII Art created by program 'Ascii Generator 2'

class TV(object):
    """Televisor"""
    def __init__(self, canal = 1, volume = 4):
        self.canal = canal
        self.volume = volume

    def play(self):
        print("%70s" % "canal {}".format(self.canal))
        print(
"""SISIS2S5XKvur:S7.7Y1PISIS5X5XIS5SIS5X5X5SIXI5IS5SIXIX5SIXIXISIS5XIXI5I
2SISI5ISIPsi  vI.:7SKS5XIS5SIS5XIS5XIXISIX2XIS5X5SIS2X5S5SIXISISISISI5
5I5I52525KXriii1v.7qqIXIS5SISI5IS5X5SI5ISI5I5I555552XISI5IX5SI5ISI5I52
I5I52525ISEv :.i.. bKXIS5SIS5XISIS5SI52S255S5SISIXISI52XISISI5ISI525IS
5252525IS5bI.:::77LbZKKSXISI5IS5S2S5S5S5S5S2X2S25ISISISISISISI5252525I
2I2525I5XqqD7:. .:.v7UX12KISI5I5IS2SI5ISISIS2525IS55IS2S2S5SIX25IS2SIS
52I25I2UJu7iir7ur:i:irbSj55XX552SI5I52SISI5I5ISI5ISIS2S25I5ISIS252S25I
UI2KSKqXvJsjL7rrudK7vErZPPKsIKI5I5I5252SI52525ISI52SII2IUS252II5I5UIII
IUqvvI2qgSMgggJ  qds JEi  rvdXPSX5S25IIISISIS25UI2II5252I252I2I2I2I2IU
5Xd ijrYi.:qggEr:q1D2YEr   rK1XbbqXKSS5SIS5SISISI55S2SI52S25ISIS2I2I2S
uuXLEruS   .sSKDXJ2ISSqu1u.  .r7YiU5qSKSXKq555525ISI5ISISI5I5ISIXI5ISI
7vvJ5 sD:: ::1ZbIKuJYJ55JPXY.  :.:i:7vsI1rrIuUsjLsLYLsLLvYLYLsYsLJvYLs
vv7vqrDU7i:.:7QuSI7i77u2:Y1UKs:   . .     vri.ivJvLvLvLvLvYvYvYvLvLvv7
vurr7KP:77.. .iIMPY::7U5.YuJs2XYriiririi:.....v:v1JjuUj1sjLsLsLsvYLYvs
JJr JKgYvUv..  vji2EdPd. 12sJsjU555I5IXIKSSsuLLr2XS1srrrYYJLYLYLsvYLYv
Ys..:r7XdggZdv     .     2uLvY7LvsvLvLLYvYvsY221i::r:ii:i777vv7v7v7vvv
Lv7ri....:75EMBDu.:    . :KYsYsYsLsYssJYjYjjS1s      sqUJvLvJsJYsYYYYL
vYY111s7i...ivr51IggBE..  U1JuYjJjsJLJJuYJ1Xr.      :Q5XKX517JujYsLsYY
LLYvsYJJ2I5.::.. :ii7j7i7.susvsLsYYvJLYYssI:.        :U: ii7L7I2jYJJjj
vLvLvLvYYjj: .Jr...    :r:Y17vvLvL7LvLvsvU: .    E:i  j        11JLJYJ
vvv7v7Lvvur   ..7ri:. ..: 7JJYYvYvYvYvLvJs:..suIIY12qQgri.     .KLLvLv
vvvsvLvLvUv :L..  rUbv  .  ujsvYLsYJYssjIrr         ...5D5jv    5Lvvvs
vLYLYLYLsJu.:LiL.  .. :i  :XuYYLYLJLJJ1s.iU:YqI2uJYri. 7vvXPLr .XjJvLv
vsvYvsLsLUs.:7:IL    .L.  rPsJJsLjYjs1Jv.I7i77i7JUIX5PK2:5Kqsr2PSjvsvL
YvLvYYsLs17 rr:Ui   .:iv7 .KsLsYJsujLrYiv1rvU1SKXsJsU1sjUKPIL7152ii1jv
vv7LvsLLvUr.ir:S: .  i71i :XsJvJsYY2i.i.rsi7LXXSbIvsjUv5UKX2v7i7X  1us
YLY7YLYLJ2i:ri:7. s  :vji YUjsJsjs1Ur.: 7sYv2j   SsvJUjs5XKJi:..U  rSs
YsYjsjsJsXi.:i:r :X  .i7. I2LsYJYJs5L.:.I77L5L   PISIXsjIK5J::.:L  .b2
uJuYJYsYJUs : .i rg. :7: :PjjsJYJsJ11  :q 7YKU:igP5II21uS55L:.r:u  LPu
YsLYLsvsjKU.:... vZ. 77  PX1sjsjYjJuU5 iY riKr  q5122I15IS2u:.irq  UIu
YLjLjsuYI7 rr... 7r  u:  7XJJYjsuYsYJP vi:L7Kv::P15uUU52SS2ui.     XKu
7v7vvvvsI. EsrJvKv   v .  J5YsLLLsssY5:iYvY2SKJS1uu1u215SSJj:q7    d21
77L7v77vX. r.:i  L.:     .2sJsJsjsJsjIr:2s1juu5ujJI251I2SuJvrK1i:  K5J
7vvLvv7Lur.  .  .EJ..   JDUuJjJjsusuJS:iiUS5:..rKSUIU5I5sIsY7XJ:i  XIu
LvYvLvvvYi. .: :Pur. .. KUJLsYsLYvJsu2:iiXP2rrijdKKIS5Xi  jrr52.:  7SY
r7r77svvYU :7: i12:.:Y..2jvjLsvYLsLJJ57 ..::i::LsUuUuIq7  j1YUu:i  vIJ
YvLvYvvvJ2.:2:.:IU7 :r.:qJJJusjsjJJYuUS.:i7LLir7ri:::.rv77rvS5Ii7::J1L
vvvvvYvLLj::Y: rU2L .r v2JLsvLvYsJvYLU7    ...:rr7iri72I1i.:iYr..LU7js
rr77v7vvJJv.L: rS1J.:: IuvvvY7Lvv7Yvj1r             : :j2Yd. .i .vj :2
ivY7rLvL7Lv.v: rujL.ii KLsvYvYYL7L7vvs:.7. :.ii .7.rP1L1LJS  Lr  .si7Y
YYLvvr7rvLU.ij.:1Jv rI.ssYJLYvvvJsJYv7  :  .:.: .r7Ys7v7vLS .Jr   ivLi
r:iv777v7v1:.Y:.j2r  ::7YjLjsY7v7vYYuv.:.   .: ...:j7v777vu..7:r..v7UU
rirr77Y7vrji    uj      ::ii:rvr777::irr7i:.ivrU1:::rri:7rr ..irrU7rvj
jI1UjuYJYvr:.J7ii7777sirrii: :Yv7rr7:.     1LYJXj77vri:irvr:..LivPuv1r
""")

    def change_canal(self, new_canal):
        try:
            new_canal = int(new_canal)
            if new_canal in range(1,1000):
                self.canal = new_canal
                print("Kanał", self.canal)
            else:
                raise ValueError
        except ValueError:
            print("błędna wartość")

    def change_volume(self, new_volume):
        try:
            new_volume = int(new_volume)
            if new_volume in range(0,11):
                self.volume = new_volume
                print("Głośność", self.volume)
            else:
                raise ValueError
        except ValueError:
            print("błędna wartość")

def main():
    tv1 = TV()
    choice = ''
    while choice != '0':
        print("""
        Telewizor

        0 - zakończ
        1 - oglądaj
        2 - zmień kanał
        3 - zmień głośność
        """)
        choice = input("Wybierasz: ")
        if choice == '1':
            tv1.play()
        elif choice == '2':
            new_canal = input("Podaj kanał 1 - 999: ")
            tv1.change_canal(new_canal)
        elif choice == '3':
            new_volume = input("Podaj głośność 0 - 10: ")
            tv1.change_volume(new_volume)
        else:
            print("błędny wybór")
        
main()
