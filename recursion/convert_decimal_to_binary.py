def convert_decimal_to_binary(n: int) -> int:
  """Convert a decimal number to its binary representation using recursion."""
  
  assert n>=0 and isinstance(n, int), 'The number has to be a positive integer only!'

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return n%2 + 10 * convert_decimal_to_binary(int(n/2))
  
print(convert_decimal_to_binary(15))