def sum_of_digits(n: int) -> int:
  """Return the sum of digits of a number using recursion."""
  
  assert n>=0 and isinstance(n, int), 'The number has to be a positive integer only!'

  if n == 0:
    return 0
  else:
    # print(n)
    print(int(n/10))
    return int(n%10) + sum_of_digits(int(n/10))
  
# print(sum_of_digits(234))
sum_of_digits(234)