class Solution(object):
    def sortedSquares(self, nums):        

        final_nums = []
        
        for i in nums :
            final_nums.append(i**2)
        
        final_nums.sort()
        return final_nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        