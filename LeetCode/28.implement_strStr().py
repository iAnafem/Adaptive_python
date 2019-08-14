"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Accepted
461,527
Submissions
1,419,752
Seen this question in a real interview before?

Yes

No
Contributor
LeetCode

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = haystack.find(needle)
        if a is None:
            raise ValueError('-1')
        else:
            return a


sol = Solution()

assert sol.strStr(haystack="hello", needle="ll") == 2
assert sol.strStr(haystack="aaaaa", needle="bba") == -1
