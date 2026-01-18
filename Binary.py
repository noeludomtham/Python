def convert(decimal_number):
    return bin(decimal_number) [2:]



decimal = int(input("Enter a decimal number: "))

binary = convert(decimal)

print( decimal, " in binary is:", binary)
