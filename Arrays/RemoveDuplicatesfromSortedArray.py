# Question: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
#
# Solution
# We basically keep a count on the number of duplicate elements
# we are removing from the array.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)

        prev = float('-inf')
        cnt = 0
        for i in range(start, end):
            if prev == float('-inf'):
                prev = nums[i - cnt]
                continue
            elif prev == nums[i - cnt]:
                del nums[i - cnt]
                cnt += 1
            else:
                prev = nums[i - cnt]
        return len(nums)