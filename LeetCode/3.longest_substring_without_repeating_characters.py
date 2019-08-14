"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# my first version


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        _dict = {}
        _max = 0
        current_max = 0
        i = 0
        while i < len(s):
            if s[i] not in _dict:
                _dict[s[i]] = i
                current_max += 1
                i += 1
            else:
                i = _dict[s[i]] + 1
                if _max < current_max:
                    _max = current_max
                current_max = 0
                _dict.clear()
        if _max < current_max:
            return current_max
        else:
            return _max


sol = Solution1()
assert sol.lengthOfLongestSubstring("ohomm") == 3
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("f") == 1
assert sol.lengthOfLongestSubstring("ffffff") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3

# my second solution


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        _dict = {}
        _max = 0
        for i in range(len(s)):
            _dict[s[i]] = 0
            for j in range(i + 1, len(s)):
                if s[j] not in _dict:
                    _dict[s[j]] = 0
                else:
                    _max = max(_max, len(_dict))
                    _dict.clear()
                    break
            if _max < len(_dict):
                return len(_dict)
        return _max


sol = Solution2()
assert sol.lengthOfLongestSubstring("ohomm") == 3
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("f") == 1
assert sol.lengthOfLongestSubstring("ffffff") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3

# The fastest solution


class Solution3:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i, value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength


sol = Solution3()
assert sol.lengthOfLongestSubstring("ohomm") == 3
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("f") == 1
assert sol.lengthOfLongestSubstring("ffffff") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
