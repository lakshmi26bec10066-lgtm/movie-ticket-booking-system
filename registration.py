# Registration module

def Registration():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    print("1. ADD THEATER DETAILS")
    print("2. UPDATE THEATER DETAILS")
    print("3. REMOVE DETAILS OF THEATER")
    print("4. SEARCH")
    print("5. GO HOME")
    op=int(input("Enter your option"))
    if op==1:
        AddTheater()
    elif op==2:
        UpdateTheater()
    elif op==3:
        RemoveTheater()
    elif op==4:
        Search()
    elif op==5:
        from homepage import Homepage
        Homepage()
    else:
        print("Invalid option")


def AddTheater():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    Tid=int(input("Enter Theater Id:"))
    Tname=input("Enter name of the Theater:")
    Tfilim=input("Enter film name:")
    Tnofront=int(input("Enter number of Seats in front row:"))
    Tnomiddle=int(input("Enter number of Seats in middle row:"))
    Tnoback=int(input("Enter number of Seats in back row:"))
    Tnobalcony=int(input("Enter number of Seats in balcony:"))
    Tpricefront=int(input("Enter price of Seat in front row:"))
    Tpricemiddle=int(input("Enter price of Seat in middle row:"))
    Tpriceback=int(input("Enter price of Seat in back row:"))
    Tpricebalcony=int(input("Enter price of Seat in balcony:"))

    from data import Theater
    Theater.append([
        Tid, Tname, Tfilim, Tnofront, Tnomiddle, Tnoback, Tnobalcony,
        Tpricefront, Tpricemiddle, Tpriceback, Tpricebalcony
    ])
    print("SUCCESSFULLY ADD THEATER DEATILS")


def UpdateTheater():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    Tid=int(input("Enter Theater Id for updation:"))
    ufilim=input("Enter film name:")
    unofront=int(input("Enter number of Seats in front row:"))
    unomiddle=int(input("Enter number of Seats in middle row:"))
    unoback=int(input("Enter number of Seats in back row:"))
    unobalcony=int(input("Enter number of Seats in balcony:"))
    upricefront=int(input("Enter price of Seat in front row:"))
    upricemiddle=int(input("Enter price of Seat in middle row:"))
    upriceback=int(input("Enter price of Seat in back row:"))
    upricebalcony=int(input("Enter price of Seat in balcony:"))

    from data import Theater
    for x in Theater:
        if x[0] == Tid:
            x[2] = ufilim
            x[3] = unofront
            x[4] = unomiddle
            x[5] = unoback
            x[6] = unobalcony
            x[7] = upricefront
            x[8] = upricemiddle
            x[9] = upriceback
            x[10] = upricebalcony
            break
    print("SUCCESSFULLY UPDATE THEATER DEATILS")


def RemoveTheater():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    Tid=int(input("Enter Id of Theater we are removing :"))

    from data import Theater
    for x in Theater[:]:
        if x[0] == Tid:
            Theater.remove(x)
            break
    print("SUCCESSFULLY REMOVE   THEATER DEATILS")


def Search():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    Tid=int(input("Enter Id of Theater we are searching :"))

    from data import Theater
    for x in Theater:
        if x[0] == Tid:
            print(x)
