try:
    num1, num2 = eval(input("Enter two numbers which are seperated by a comma: "))
    result = num1 / num2
    print("Result is ",result)
except ZeroDivisionError:
    print("Division by zero will cause an error!")
except SyntaxError:
    print("Comma is missing. Please insert a comma in between like this: 1, 2!")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will always execute")