"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if s:
            stack = []
            _dict = {')': '(', ']': '[', '}': '{'}
            for char in s:
                if char not in _dict:
                    stack.append(char)
                elif char in _dict and len(stack) == 0:
                    return False
                else:
                    if stack[-1] == _dict[char]:
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
        return True


sol = Solution()
assert sol.isValid('') is True
assert sol.isValid('()') is True
assert sol.isValid('()[]{}') is True
assert sol.isValid('(]') is False
assert sol.isValid('([)]') is False
assert sol.isValid('{[]}') is True
assert sol.isValid('[])') is False


class Solution2:
    def isValid(self, s: str) -> bool:
        if s:
            stack = []
            for char in s:
                if char not in ')}]':
                    stack.append(char)
                elif char in ')}]' and len(stack) == 0:
                    return False
                else:
                    if (
                            stack[-1] == '(' and char == ')' or
                            stack[-1] == '[' and char == ']' or
                            stack[-1] == '{' and char == '}'
                    ):
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
        return True


sol = Solution2()
assert sol.isValid('') is True
assert sol.isValid('()') is True
assert sol.isValid('()[]{}') is True
assert sol.isValid('(]') is False
assert sol.isValid('([)]') is False
assert sol.isValid('{[]}') is True
assert sol.isValid('[])') is False



