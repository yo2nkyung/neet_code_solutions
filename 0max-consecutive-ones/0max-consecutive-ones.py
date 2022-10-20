class Solution(object):
    def findMaxConsecutiveOnes(self, nums):    
        count = 0
        max_count = 0

        for i in nums:
            if i == 0 :
                count = 0
            else : 
                count += 1
                if count > max_count :
                    max_count = count
        
        return max_count
                
        """
        :type nums: List[int]
        :rtype: int
        """
        