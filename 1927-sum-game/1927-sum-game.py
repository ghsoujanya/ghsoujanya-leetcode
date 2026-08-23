class Solution:

  def sumGame(self, num: str) -> bool:
    n = len(num)
    mid = n // 2

    left_str = num[:mid]
    right_str = num[mid:]

    sum_left = sum(int(c) for c in left_str if c != "?")
    sum_right = sum(int(c) for c in right_str if c != "?")

    q_left = left_str.count("?")
    q_right = right_str.count("?")

    # If the total number of '?' is odd, Alice always wins
    if (q_left + q_right) % 2 != 0:
      return True

    # Bob wins iff the sum difference equals 9.0 * (q_right - q_left) / 2
    return (sum_left - sum_right) * 2 != 9 * (q_right - q_left)