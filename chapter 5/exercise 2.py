# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 5, exercise 2

stats={"total":int(30),
       "strength":int(0),
       "health":int(0),
       "wisdom":int(0),
       "dexterity":int(0)}

choice=None
while choice!='5':
    print("*****************************")
    print("Kreator postaci")
    print("%2s" % stats["total"], "- pozostało punktów\n")

    print("%2s" % stats["strength"], "- Siła")
    print("%2s" % stats["health"], "- Zdrowie")
    print("%2s" % stats["wisdom"], "- Mądrość")
    print("%2s" % stats["dexterity"], "- Zręczność")

    print("\n1 - zmień siłę")
    print("2 - zmień zdrowie")
    print("3 - zmień mądrość")
    print("4 - zmień zręczność")
    print("5 - zakończ")

    choice=input("\nWybierasz: ")

    if choice=='1':
        new_stat=int(input("Siła: "))
        if (new_stat<=stats["total"]+stats["strength"]) and new_stat>=0:
            stats["total"]+=stats["strength"]
            stats["strength"]=new_stat
            stats["total"]-=new_stat
        else:
            print("\n--- BŁĘDNA WARTOŚĆ ---\n")
            
    elif choice=='2':
        new_stat=int(input("Zdrowie: "))
        if (new_stat<=stats["total"]+stats["health"]) and new_stat>=0:
            stats["total"]+=stats["health"]
            stats["health"]=new_stat
            stats["total"]-=new_stat
        else:
            print("\n--- BŁĘDNA WARTOŚĆ ---\n")
            
    elif choice=='3':
        new_stat=int(input("Mądrość: "))
        if (new_stat<=stats["total"]+stats["wisdom"]) and new_stat>=0:
            stats["total"]+=stats["wisdom"]
            stats["wisdom"]=new_stat
            stats["total"]-=new_stat
        else:
            print("\n--- BŁĘDNA WARTOŚĆ ---\n")
            
    elif choice=='4':
        new_stat=int(input("Zręczność: "))
        if (new_stat<=stats["total"]+stats["dexterity"]) and new_stat>=0:
            stats["total"]+=stats["dexterity"]
            stats["dexterity"]=new_stat
            stats["total"]-=new_stat
        else:
            print("\n--- BŁĘDNA WARTOŚĆ ---\n")
