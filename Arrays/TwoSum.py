# Question: Two Sum
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/
#
# Solution
# If we sort the elements - the maximum sum can be formed by using numbers at the
# last two index positions. Minimum sum can be formed by using the numbers at the
# first two index positions.
# Binary Search:
# We can rather start with a middle value -> by using first and last
# index position. This gives us idea every time if we need to move the first
# position pointer forward or move the last position pointer backward.
# The only caveat here to look at is that we have to return the original indices.


# ex => A = [ 1, 3, 4, 5, 7]  Sum = 6
# Initial:  i=0,  j=4, A[i] = 1, A[j] = 7
# A[i] + A[j] = 8 > 6
# so we need to move the last position pointer backward in order to search for a smaller sum.

# Approach 1: [Doesn't work]
# where we use in-built sorting => we are likely to fail where we have duplicates in the array =>
# A = [3, 3]
# sorted_A = [ 3, 3]
# but when we use index() on the list element, it will always return the first found index
# which is not correct. So, we need to map the original indexes as well before applying a sort.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        # Sort the array.
        nums_sorted = sorted(nums)

        i = 0
        j = len(nums_sorted) - 1

        while (i < j):
            sum = nums_sorted[i] + nums_sorted[j]
            if sum == target:
                return [nums.index(nums_sorted[i]), nums.index(nums_sorted[j])]
            elif sum > target:
                j -= 1
            else:
                i += 1

        return []

# Approach 2: We store the index positions of the elements in the original array
# and create a list of lists while keeping the logic of finding sum in the
# sorted array similar to the approach 1.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        nums_pair_l = []
        for ind in range(0, len(nums)):
            nums_pair_l.append([nums[ind], ind])

        # Sort the list of lists.
        nums_pair_l.sort()

        i = 0
        j = len(nums_pair_l) - 1

        while (i < j):
            sum = nums_pair_l[i][0] + nums_pair_l[j][0]
            if sum == target:
                return [nums_pair_l[i][1], nums_pair_l[j][1]]
            elif sum > target:
                j -= 1
            else:
                i += 1

        return []