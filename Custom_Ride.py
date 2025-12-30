print("Select a vehicle: ")
print("1.Bike")
print("2.Car")
choice=int(input("Enter your choice: "))

if(choice == 1): 
    print("What type of bike?")
    print("1.Scooty")
    print("2.Scooter")
    choice2=int(input("Enter your choice2: "))
    if choice2 == 1:
        print("You have selected the Scooty")
    else:
        print("You have selected the Scooter")


elif(choice == 2):
    print("What type of car?")
    print("1.Standard Car")
    print("2.Electric Car")
    choice3=int(input("Enter your choice3: "))
    if choice3 == 1:
        print("You have selected the Standard Car")
    else:
        print("You have selected the Electric Car")
    
else:
    print("Please enter either 1 or 2")