# Ticket booking module

def TicketBooking():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    print("1. Ticket Booking")
    print("2. Ticket Cancellation")
    print("3. Search Booking details")
    print("4. Go Home page")
    op=int(input("Enter your option"))
    if op==1:
        Tbooking()
    elif op==2:
        Tcancel()
    elif op==3:
        SearchBooking()
    elif op==4:
        from homepage import Homepage
        Homepage()
    else:
        print("Invalid option")


def Tbooking():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")

    from data import Theater
    print("DEtails of Theaters ")
    for x in Theater:
        print(x)

    bid=int(input("Enter Booking id"))
    tid=int(input("Enter Theater id:"))
    typeticket=input("Enter type of ticket(Front/Middle/Back/Balcony)")

    fare=0
    for x in Theater:
        if x[0] == tid:
            if typeticket=="Front":
                fare=x[7]
            elif typeticket=="Middle":
                fare=x[8]
            elif typeticket=="Back":
                fare=x[9]
            elif typeticket=="Balcony":
                fare=x[10]
            break

    from data import ticketbooking
    ticketbooking.append([bid, tid, typeticket, fare])
    print("Successfully Booking done")


def Tcancel():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")

    bidcan=int(input("Enter id of the ticket  to be cancelling:"))
    from data import ticketbooking, Theater

    typeticket=""
    tidcan=None

    for x in ticketbooking:
        if x[0] == bidcan:
            typeticket=x[2]
            tidcan=x[1]
            print(typeticket)
            break

    for x in ticketbooking[:]:
        if x[0] == bidcan:
            ticketbooking.remove(x)
            break

    for x in Theater:
        if x[0] == tidcan:
            if typeticket=="front":
                x[3]=x[3]+1
            elif typeticket=="middle":
                x[4]=x[4]+1
            elif typeticket=="back":
                x[5]=x[5]+1
            elif typeticket=="balcony":
                x[6]=x[6]+1
            break

    print("SUCCESSFULLY DONE THE CANCELLATION OF TICKET")


def SearchBooking():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")

    bidcan=int(input("Enter id of the ticket booking to be searching: "))
    from data import ticketbooking

    myrecord=[]
    for x in ticketbooking:
        if x[0] == bidcan:
            myrecord.append(x)

    print("Bookingid\tTheaterId\tTypeofseat\tprice\n")
    for x in myrecord:
        print(x[0],"\t",x[1],"\t",x[2],"\t",x[3],"\n")
