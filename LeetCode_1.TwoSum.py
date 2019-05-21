"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
    _hash = dict()
    for i, j in enumerate(nums):
        _hash[j] = i
    for num in range(len(nums)):
        x = target - nums[num]
        if x in _hash and num != _hash[x]:
            return [num, _hash[x]]


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 5, 1], 6) == [1, 2]
