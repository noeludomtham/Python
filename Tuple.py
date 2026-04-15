def multiply_tuple(tup):
    product = 1
    for num in tup:
        product = product* num
    return product

numbers = (2, 3, 4, 5)

result = multiply_tuple(numbers)
print("Product of tuple elements:", result)