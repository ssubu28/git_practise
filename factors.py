"""
Program to find all the factors of a number
"""
#from time import time
#from functools import reduce

def factors_num(number):
    new_list = []

    # Approach 1:
    if number <= 1:
        return new_list.append(number)

    # Need to stop iterating when you get a hit on searching the number in new_list  (OR) 
    # Loop till srqt(no) and not till number//2 as one of the factors will be smaller than the sqrt val.
    
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            if (number//i) not in new_list and (i not in new_list):
                new_list.append(number//i)
                new_list.append(i)
            else:
                return new_list

    return new_list



"""
# Online solution:
def factors_func(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
""" 


number = input("Enter a number: ")

print(f"The factors of a number are: {sorted(factors_num(int(number)))}")



"""
start2 = time()
print(f"Start time for online code: {start2}")
print(f"The factors of a number are: {factors_func(int(number))}")
end2 = time()
print(f"Time taken for online code: {end2 - start2}")
"""