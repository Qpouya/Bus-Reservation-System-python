print("\n\nWelcome! To Ticket Booking System\n")
restart = ('Y')
while restart != ('N' ,'NO' ,'n' ,'no'):
    print("1.Check pnr status")
    print("2.Ticket Reservation")
    option = int(input("\nEnter your option : "))

    if option == 1:     #choose 1 to quit program
        print("Your pnr status is t2") #choose 2 test program
        exit(0)
    elif option==2:
        numberofbus=int(input("\nEnter number of bus : "))
        numberofpassengers=int(input("\nEnter number of passengers : "))
        driver_name=[]
        seats_number=[]
        arrival_time=[]
        departure_time=[]
        start1=[]
        destination=[]
        passenger_name = []
        bus_available=[]
        bus_notavailable=[]
        number_wanted=[]
        havefoundbus=[]
        for p in range(numberofbus):
            name = str(input("\nName of driver : "))
            driver_name.append(name)
            numberofseats=int(input("\nNumber of seats : "))
            seats_number.append(numberofseats)
            time1= str(input("\nArrivaltime  : "))
            arrival_time.append(time1)
            time2=str(input("\nDeparturetime : "))
            departure_time.append(time2)
            mabda=str(input("\nPlace of start : "))
            start1.append(mabda)
            des=str(input("\nDestination : "))
            destination.append(des)
        restart = str(input("\nOops! Forget someone : "))
        if restart in ('y', 'YES', 'yes', 'Yes'):
            restart = ('Y')
        else:
            x=0
            print("\nTotal buses : ",numberofbus)
            for p in range(1, numberofbus+1):
                print("Bus : ", p)
                print("Name of driver : ", driver_name[x])
                print("Number of seats : ", seats_number[x])
                print("Arrival time : ", arrival_time[x])
                print("Departure time : ", departure_time[x])
                print("Start : ", start1[x])
                print("Destination : ", destination[x])
                x +=1

        for i in range(numberofpassengers):
            name2=str(input("\nEnter passenger name : "))
            passenger_name.append(name2)
            whichbus=str(input("\nWhich is suitable for you((already in bus list)\ nothing) ? ")) #choose from name of drivers, or
            if whichbus=='nothing':              #choose nothing if none of above is suitable for you
                bus_notavailable.append(whichbus)
                print("\nSorry there is no bus available for you")
            else:
                bus_available.append(whichbus)
                wantednummber = int(input("\nEnter which number you want to reserve : "))
                number_wanted.append(wantednummber)
                havefoundbus.append(name2)
                m=len(havefoundbus)

        restart = str(input("\nOops! Forget someone : "))
        if restart in ('y', 'YES', 'yes', 'Yes'):
            restart = ('Y')
        else:
            x = 0
            print("\nNumber of passengers who have found bus:  ",m)
            for i in range(1,m+1):
                print("Passenger : ",havefoundbus[x])
                print("which bus : ",bus_available[x])
                print("Reserved seat : ",number_wanted[x])
                x+=1




























        
