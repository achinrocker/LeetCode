# Question: Single Number
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
#
# Solution
# We basically do a XOR on all the elements.
# If we take XOR of zero and some bit, it will return that bit
# => X ^ 0 = X
# If we take XOR of two same bits, it will return 0
# => X ^ X = 0
# => X ^ Y ^ X = (X ^ X) ^ Y = 0 ^ Y = Y
# so all the repeated elements except the unique non-repeated
# element are cancelled out.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans