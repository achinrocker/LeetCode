# Question: Contains Duplicate
#
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
#
# Solution
# Approach is quite simple => if we sort the array, we need to just check if any of the
# next number is same as the previous encountered number.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        sorted_nums = sorted(nums)
        prev = float('inf')
        for num in sorted_nums:
            if prev == float('inf'):
                prev = num
            elif prev == num:
                return True
            else:
                prev = num

        return False