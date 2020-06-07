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
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False