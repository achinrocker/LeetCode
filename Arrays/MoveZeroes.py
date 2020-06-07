# Question: Move Zeroes
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
#
# Solution
# Approach 1.
# One simple approach is to delete zeroes and append same number of zeroes
# at the end.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(0, len(nums)):
            if nums[i - cnt] == 0:
                del nums[i - cnt]
                cnt += 1

        for i in range(cnt):
            nums.append(0)

# Solution
# Approach 2.
# Other approach is to use two pointers.
