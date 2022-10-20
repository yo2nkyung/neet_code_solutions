class Solution(object):
    def findNumbers(self, nums):
        total_count = 0
        
        for i in range(len(nums)) :
            count = 0
            number = nums[i]
            while number > 0 :
                number //= 10
                count += 1
            if count % 2 == 0:
                total_count += 1
        
        return total_count
        """
        :type nums: List[int]
        :rtype: int
        """
        