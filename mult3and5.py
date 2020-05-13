"""
Code Kata:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.

"""

def solution(number):
  total_sum = 0
  
  for i in range(1, number):
      if (i % 3 == 0 and i % 5 != 0) or (i % 3 != 0 and i % 5 == 0):
          total_sum += i
      elif i % 3 == 0 and i % 5 == 0:
          total_sum += i
      elif i % 3 != 0 and i % 5 != 0:
          pass
  print(total_sum)


number = int(input("Please enter a number: "))
solution(number)