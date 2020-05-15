"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""


from datetime import datetime

age = int(input("Enter your age as a number: "))

new_age_year = datetime.now().year + (100 - age)

age_output = f"You will turn 100 in the year {new_age_year}"
print(age_output)

copies = int(input("Enter another number to create copies: "))

# To find alternate to for loop here. Use age_output*copies but print on new line. 

for i in range(copies):
    print(f"{age_output}")



