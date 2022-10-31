class Solution(object):
    def moveZeroes(self, nums):
        
        read_pointer = 0
        write_pointer = 1
        while read_pointer < len(nums) and write_pointer < len(nums) :
            
            if nums[read_pointer] == 0 and nums[write_pointer] == 0:
                write_pointer += 1
                
            elif nums[read_pointer] == 0 and nums[write_pointer] != 0:
                tmp = nums[read_pointer]
                nums[read_pointer] = nums[write_pointer]
                nums[write_pointer] = tmp
                read_pointer += 1
                write_pointer += 1

            else:
                read_pointer += 1
                write_pointer += 1
        
        return nums
            
                
       
        '''
        if nums[0] == 0 and if nums[0+1] != 0:
            tmp = nums[0]
            nums[0] = nums[0+1]
            nums[0+1] = tmp

        pointer += 1
        '''
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        