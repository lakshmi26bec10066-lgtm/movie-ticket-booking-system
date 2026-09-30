# Login module

def Login():
    print("\n\n\n\n")
    print("************************************")
    print("WELCOME TO BOOK MY SHOW")
    print("*************************************")
    user=input("Enter USER ID:")
    pas=input("Enter PASSWORD:")
    if user=="Admin" and pas=="mgm":
        print("SUCCESSFULLY LOGGED !!!!")
        from homepage import Homepage
        Homepage()
    else:
        print("INCORRECT CREDENTIALS")
        Login()
