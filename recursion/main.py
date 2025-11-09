import sys

# Increase the recursion limit
sys.setrecursionlimit(1000)

def factorial(number: int):
  assert number >= 0 and int(number) == number, 'The number must a positive integer only!'

  if number in [0,1]:
    return 1
  else:
    return number * factorial(number-1) # recursively calculate the factorial

print(factorial(5))

## Recursion vs Iteration ###
def powerOfTwo(n: int) -> int:
    if n == 0:
      return 1
    else:
      power = powerOfTwo(n-1)
      return power * 2

print(powerOfTwo(3))

def powerOfTwoIt(n: int) -> int:
    i = 0
    power = 1
    while i < n:
      power = power * 2
      i = i + 1
    return power


print(powerOfTwoIt(4))