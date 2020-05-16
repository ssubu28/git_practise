"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""



def odd_even(number1):
    if number1 % 2 == 0:
        if number1 % 4 == 0:
            print(f"The number {number1} is even and divisible by 4!")
        else:
            print("The number {number1} is an even number.")
    else:
        print("The number {number1} is an odd number.")


def divisible(number1, number2):
    if number1 % number2 == 0:
        print(f"Check {number2} divides number {number1} evenly.")
    else:
        print(f"Check {number2} does not divide number {number1} evenly.")




number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))


odd_even(number1)
divisible(number1, number2)



