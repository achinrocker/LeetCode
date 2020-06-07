# Question: Plus One
# Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
#
# Solution
# Approach is quite simple => we need to iterate the array backwards.
# For the same we can either use range(len(list)-1, -1, -1) or use reversed(list).
# Max carry can be 1 here => 9 + 9 = 18, digit = 18 % 10 = 8, carry = 1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Plus One
        carry = 1

        for ind in range(len(digits) - 1, -1, -1):
            digits[ind] += carry
            carry = 0

            if digits[ind] >= 10:
                digits[ind] = digits[ind] % 10
                carry = 1

            if carry == 0:
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits