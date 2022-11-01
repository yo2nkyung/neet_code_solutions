class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        