import random

print("*" * 20, "\n")
print("\nWELCOME TO TRAIN RESERVATION SYSTEM\n")
print("*" * 20, "\n")

#stations = ["DELHI", "GWALIOR", "CHENNAI", "BANGALORE", "BOMBAY", "KOLKATA", "PATNA"]
#destination = ["JAMMU"]

lst = list()
for i in range(1, 72):
    lst.append(i)
    fname = list()
for j in range(1, 72):
    fname.append(j)
    lname = list()
for k in range(1, 72):
    lname.append(k)
    agep = list()
for i in range(1, 72):
    agep.append(i)

r = 1
while r != 0:
    print("\n1.BOOK TICKET")

    def BOOK_TICKETS():
        src = input("ENTER SOURCE: ")
        dest = input("Enter Destination: ")
        tier = input("Select Tier: ")

        coach_no = random.randint(1,3)
        seat_no = random.randint(0, 54)

        print("YOUR TICKET FROM", src, "TO", dest, "IS GETTING PROCESSED!!")
        print("PLEASE ENTER THE FOLLOWING DETAILS")
        if lst[seat_no - 1] == seat_no:
            fname1 = str(input("Enter Your First Name: \n"))
            lname1 = str(input("Enter Your Last Name: \n"))
            age1 = int(input("Enter Your age: \n"))
            lst.pop(seat_no - 1)
            fname.pop(seat_no - 1)
            agep.pop(seat_no - 1)
            lst.insert(seat_no - 1, 'B')
            fname.insert(seat_no - 1, fname1)
            lname.insert(seat_no - 1, lname1)
            agep.insert(seat_no - 1, age1)

            print("Your ticket is booked")
            print("Seat Details : A",coach_no, seat_no)

        else:
            print("\n **")
            print("Seat is already booked try other seat")
            print("**\n")

        # else:
        #    print("enter the valid station name")


    print("2.CHECK TICKET STATUS")


    def SEAT_AVAILABILITY():
        print("Available Seats: ", 54-1)
        #for seat_no not in lst:
            #print(seat_no, end=" ")


    print("3.CANCEL TICKET")

    def CANCEL_TICKETS():
        tic = int(input("Enter Seat Number:"))
        if lst[tic - 1] == tic:
            print("\n**")
            print("This seat is not Booked")
            print("*\n")
        else:
            lst.pop(seat_no - 1)
            lst.insert(tic - 1, tic)
            print("\n**")
            print("Your ticket is cancelled")
            print("*\n")


    print("4.CHECK DETAILS OF BOOKED TICKET")

    def CHECK_DETAILS():
        s = int(input("Enter Seat number:\n"))
        s = s - 1
        if fname[s] == s + 1:
            print("\n**")
            print("This seat is not Booked")
            print("*\n")
        else:
            print("\n**")
            print(f"Customer Name is: {fname[s].title()} {lname[s].title()} and Age is: {agep[s]}")
            print("*\n")

    print("5.EXIT")

    choice = int(input("\n Enter Your Option:"))
    if choice == 1:
        BOOK_TICKETS()
    elif choice == 2:
        SEAT_AVAILABILITY()
    elif choice == 3:
        CANCEL_TICKETS()
    elif choice == 4:
        CHECK_DETAILS()
    elif choice == 5:
        r = 0
        exit()
    else:
        print("\n**")
        print("You have chosen wrong option!!\n")
        print("*\n")
