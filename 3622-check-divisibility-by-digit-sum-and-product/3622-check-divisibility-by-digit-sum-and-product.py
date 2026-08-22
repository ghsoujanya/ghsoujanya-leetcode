class Solution:

  def checkDivisibility(self, n: int) -> bool:
    digits = [int(d) for d in str(n)]
    digit_sum = sum(digits)

    from math import prod

    digit_prod = prod(digits)

    return n % (digit_sum + digit_prod) == 0