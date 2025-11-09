def greatest_common_divisor(a, b):
    """Return the greatest common divisor of a and b using recursion."""
    assert isinstance(a, int), 'First number has to be a positive integer only!'
    assert isinstance(b, int), 'Second number has to be a positive integer only!'

    if a < 0:
       a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
      return greatest_common_divisor(b, a%b)

print(greatest_common_divisor(48, 18))