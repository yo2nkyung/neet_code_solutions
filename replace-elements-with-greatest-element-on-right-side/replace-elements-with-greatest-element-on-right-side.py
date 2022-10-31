class Solution(object):
    def replaceElements(self, arr):
        result = [0] * len(arr)
        result[-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            result[i] = max([result[i+1], arr[i+1]])
        
        return result
        """
        :type arr: List[int]
        :rtype: List[int]
        arr = [17,18,5,4,6,1]
        """
        