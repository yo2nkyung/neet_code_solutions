class Solution(object):
    def thirdMax(self, nums):
        
        expected = sorted(nums, reverse=True)
        largest = expected[0]

        count = 0
        
        for i in range(1, len(expected)):

            if expected[i] < largest:
                largest = expected[i]
                count += 1
            if count == 2:
                break
        
        if count < 2 or len(expected) < 3:
            largest = expected[0]
        
        return largest
                
        """
        :type nums: List[int]
        :rtype: int
        """
        