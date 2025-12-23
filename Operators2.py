a = 10
b = 12
c = 0

if a and b and c:
    print("All the numbers have have a boolean value as True")
else:
    print("At least on of the numbers have a boolean value as False")


a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either number is greater than 0")
else:
    print("No number is greater than 0")



a = 10
b = 12
c = 12

print(a !=b)
print(b != c)

a = "python"
b = "coding"

if a != b :
    print(a, 'and', b, 'are different.')

a = 4
a = 5

if (a == 1) != (b == 5):
    print("Hello")

a = int(input("enter a number"))

if a%2 != 0 :
    print(a, "is not an even number")