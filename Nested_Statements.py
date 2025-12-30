medical_cause=input("Did you have a medical cause? Y/N: ")
atten=int(input("Enter the attendance of the student: "))

if medical_cause == 'Y' :
    print("You are allowed to take the exam!")
else:
    if atten>=75:
        print("You are allowed to take the exam!")
    else:
        print("You may not take the exam!")