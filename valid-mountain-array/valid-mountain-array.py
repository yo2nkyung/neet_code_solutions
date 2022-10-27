class Solution(object):
    def validMountainArray(self, arr):
        if (len(arr) < 3) or (arr[0] > arr[1]) or (arr[len(arr) - 1] > arr[len(arr) - 2]):
            return False
        
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                return False
        
        for i in range(len(arr) - 2):
            if arr[i] > arr[i+1] and arr[i+1] < arr[i+2]:
                return False
            
        
            
        
        return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        