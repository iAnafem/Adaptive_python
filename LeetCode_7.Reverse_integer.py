"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,
  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

# First solution


class Solution:
    @staticmethod
    def reverse(x):
        result = []
        for d in str(x):
            result.insert(0, d)
        if x < 0:
            result.pop()
            if int("".join(result)) > 2147483647:
                return 0
            return -int("".join(result))
        else:
            if int("".join(result)) > 2147483647:
                return 0
            return int("".join(result))

# Second solution


class Solution2:
    @staticmethod
    def reverse(x):
        int_max = 2147483647
        int_min = -2147483648
        rev = 0
        negative = 1
        if x < 0:
            x = abs(x)
            negative = -1
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > int_max // 10 or rev == int_max / 10 and pop > 7:
                return 0
            if rev * negative < int_min // 10 or rev * negative == int_min / 10 and pop < -8:
                return 0
            rev = rev * 10 + pop
        return rev * negative


