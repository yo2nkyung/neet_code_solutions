class Solution(object):
    def duplicateZeros(self, arr):
        arr_tmp = []
        
        for num in arr :
            if num == 0 :
                arr_tmp.append(num)
            arr_tmp.append(num)
                
        for i in range(len(arr)) :
            arr[i] = arr_tmp[i]
        
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        