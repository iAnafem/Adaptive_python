"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        elif len(set(strs)) == 1:
            return strs[0]
        max_prefix = min(strs)
        for i, j in enumerate(max_prefix):
            for k in strs:
                if k[i] != j:
                    return max_prefix[:i]
        return max_prefix


s = Solution()
print(s.longestCommonPrefix(["", ""]))
print(s.longestCommonPrefix(["flight", "flight", "flight"]))
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""



