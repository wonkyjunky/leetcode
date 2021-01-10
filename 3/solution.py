# Leetcode: Rotate Array
# the key point is you don't really need to rotate.
# just get last k number of integers from the list and put it to nums
# and get intergers from the list without the last k numbers of integers and 
# add them together. 

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
            