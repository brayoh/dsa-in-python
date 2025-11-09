def fibonacci(n: int):
  """Return the nth Fibonacci number using recursion."""
  
  assert n >= 0 and isinstance(n, int), "Fibonacci number cannot be a negative number or non-integer"

  if n in [0,1]:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
print(fibonacci(6))