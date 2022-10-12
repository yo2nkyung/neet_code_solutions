class Solution(object):
    def fizzBuzz(self, n):
        array = []
        for i in range(0,n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                array.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                array.append("Fizz")
            elif (i+1) % 5 == 0:
                array.append("Buzz")
            else: array.append(str(i+1))
            
        return array
        """
        :type n: int
        :rtype: List[str]
        """