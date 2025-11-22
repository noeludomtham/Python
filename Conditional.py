num = 3
if num > 0:
    print(num, "is a positive number")

num = -1
if num > 0:
    print(num, "is a positive number")
else:
    print(num, "is a negative number")


actual_cost = float(input("Please enter the actual sales price:"))
sale_amount = float(input("Please enter the sales amount:"))

if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Your total profit is = {0}".format(amount))
else:
    print("You lost profit...")


i = int(input("Enter a number :"))
if (i < 15):
    print("i is smaller than 15")
    print("im in the if block")
else:
    print("i is bigger than 15")
    print("im in the else block")
print("im not in the if or else block")


number = int(input("Enter the number you want to check:"))
print("Number to be checked:", number)
if number%2==0:
    print("This is an even number")
else:
    print("This is an odd number")