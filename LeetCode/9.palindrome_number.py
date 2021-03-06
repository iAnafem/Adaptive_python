"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?

"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        prev = x
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        return prev == rev


print(Solution.isPalindrome(121))
print(Solution.isPalindrome(-121))
print(Solution.isPalindrome(122))
print(Solution.isPalindrome(10))
