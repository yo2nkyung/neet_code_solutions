class Solution(object):
    def removeDuplicates(self, nums):
        
        duplicate = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate += 1
            else:
                nums[i - duplicate] = nums[i]
                
        return len(nums) - duplicate
                
        """
        :type nums: List[int]
        :rtype: int
        """
        