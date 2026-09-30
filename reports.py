# Report module

def Report():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    print("1. Report Based on Types of seats")
    print("2. Report Based on Ticket price")
    print("3.GO HOME ")
    op=int(input("Enter your option:"))

    if op==1:
        from data import ticketbooking
        typeseat=[]
        noseat=[]
        counts={}
        for x in ticketbooking:
            seat=x[2]
            counts[seat]=counts.get(seat,0)+1
        for seat,count in counts.items():
            typeseat.append(seat)
            noseat.append(count)

        import matplotlib.pyplot as plt
        plt.bar(typeseat,noseat)
        plt.xlabel("Type of seat")
        plt.ylabel("No of seats")
        plt.title("Grpah based on Type and No of seats")
        plt.show()

    elif op==2:
        from data import ticketbooking
        typeseat=[]
        noseat=[]
        totals={}
        for x in ticketbooking:
            seat=x[2]
            totals[seat]=totals.get(seat,0)+x[3]
        for seat,total in totals.items():
            typeseat.append(seat)
            noseat.append(total)

        import matplotlib.pyplot as plt
        plt.bar(typeseat,noseat)
        plt.xlabel("Type of seat")
        plt.ylabel("Total Amount")
        plt.title("Grpah based on Type and Amount for each type")
        plt.show()

    elif op==3:
        from homepage import Homepage
        Homepage()
