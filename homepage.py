# Homepage module

def Homepage():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    print("************************************")
    print("1. Registration Session")
    print("2. Ticket Booking")
    print("3. SEARCH")
    print("4. REPORT")
    op=int(input("Enter Your option:"))
    if op==1:
        from registration import Registration
        Registration()
    elif op==2:
        from booking import TicketBooking
        TicketBooking()
    elif op==3:
        from registration import Search
        Search()
    elif op==4:
        from reports import Report
        Report()
    else:
        print("INVALID OPTION")
