"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution:
    def myPow(self, x, n):
        negative = 1
        sign = 1
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = abs(n)
            negative = -1
        if x < 0 and n % 2 != 0:
            x = abs(x)
            sign = -1
        mod = 1000000007
        if n % 2 == 0:
            result = self.myPow(x, int(n / 2))
            return float((result * result) % mod) ** negative * sign
        else:
            return float((self.myPow(x, n - 1) * x) % mod) ** negative * sign


s = Solution()
print(s.myPow(2.00000, 10))
print(s.myPow(2.00000, -2))
print(s.myPow(-13.62608, 3))
