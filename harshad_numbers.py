# Harshad numbers

"""
# Working

def is_valid(number):
    if number == 0:
        return "Not allowed: Division by zero!"

    total_sum = 0
    number_copy = number

    while number_copy > 1:
        r = number_copy % 10
        total_sum += r
        number_copy = number_copy // 10

    total_sum += number_copy

    if number % total_sum == 0:
        return True
    else:
        return False
"""

def get_next(number):
    if number == 0:
        return "Not allowed: Division by zero!"

    total_sum = 0
    number_copy = number

    while number_copy > 1:
        r = number_copy % 10
        total_sum += r
        number_copy = number_copy // 10

    total_sum += number_copy

    if number % total_sum == 0:
        print(number)
        return number  # recursive loop so return will only go one level up. Need to exit code.  -- HOW ?
        
    else:
        number += 1
        get_next(number)


    

number = int(input("Enter a valid integer: "))
#print(is_valid(number))


res = get_next(number)
print(res)