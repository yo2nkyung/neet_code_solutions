# Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
```
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]

// Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
```

Example 2:
```
Input: nums = [4,5,6], target = 10
Output: [0,2]
```

Example 3:
```
Input: nums = [5,5], target = 10
Output: [0,1]
```

## Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} //dictionary
        
        for i, n enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
// hashmap(in python, it is dictionary) time complexity: O(1) 
```

## Result
Time and Space Complexity
* Time Complexity: O(n)
  * The solution iterates through `nums` once, performing O(1) operations (dictionary lookup and insertion) for each element.
* Space Complexity: O(n)
  * The dictionary `prevMap` stores at most `n` elements.
