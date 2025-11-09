def power_of_numbers(base: int, exp: int) -> int:
  """Return base raised to the power of exp using recursion."""
  
  assert isinstance(base, int) and base >= 0, 'Base has to be a positive integer only!'
  assert isinstance(exp, int) and exp >= 0, 'Exponent has to be a positive integer only!'

  if exp == 0:
    return 1
  elif exp == 1:
    return base
  else:
    return base * power_of_numbers(base, exp-1)

print(power_of_numbers(0,0))