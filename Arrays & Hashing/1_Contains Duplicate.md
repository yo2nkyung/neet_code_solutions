# 1. Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

---

## Solution
```
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

* Parameters:
    * `self`: Refers to the instance of the class.
    * `nums: List[int]`: A list of integers. `List[int]` is type hinting to indicate that the input is a list of integers.
* Return type: `-> bool` indicates the function returns a Boolean value (True or False).


## Result
- Time & Space Complexity
    - Time complexity: O(n)
    - Space complexity: O(n)
