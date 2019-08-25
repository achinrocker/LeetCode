# https://leetcode.com/problems/longest-increasing-subsequence/
# This is not the most optimal approach O(N^2) for solving the problem,
# a better solution could be O(N Log N) using balanced binary trees.
# Will update this in LIS2.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ans = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] <= nums[i]:
                    ans[i] = max(ans[i], ans[j]+1)
        #print(ans)
        return max(item for item in ans)
