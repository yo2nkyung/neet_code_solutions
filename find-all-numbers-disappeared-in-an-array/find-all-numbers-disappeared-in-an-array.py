class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = set(range(1, len(nums)+1))
        
        nums = set(nums)
        
        result = result - nums
        #포문을 2 개 돌리니 시간 초과. 포문을 사용하지 않는 방향으로 수정
        #파이썬 자료형 set을 사용
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        