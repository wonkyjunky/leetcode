# Leetcode : Find Pivot Index


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):
            a = sum(nums[:x])
            b = sum(nums[x+1:])
            if (a == b):
                return x
            
        return -1