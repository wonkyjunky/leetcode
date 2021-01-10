# Leetcode : Remove Duplicates from Sorted Array
# Slow and Fast (two pointer approach)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        slow = fast = 0
        
        while fast <= len(nums) - 1:
            if (nums[fast] != nums[slow]):
                nums[slow+1] = nums[fast]
                slow = slow + 1
            fast = fast + 1
            
        return slow + 1
            
            