# 4. Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
```
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```
Example 2:
```
Input: strs = ["x"]
Output: [["x"]]
```
Example 3:
```
Input: strs = [""]
Output: [[""]]
```

Constraints:

1 <= strs.length <= 1000.

0 <= strs[i].length <= 100

strs[i] is made up of lowercase English letters.

## Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # Use tuple(count) as the key for grouping
        return list(res.values()) # Return grouped anagrams as a list of lists
```

## Result
Time & Space Complexity
* Time complexity: O(m ∗ n)
* Space complexity: O(m)
> Where `m` is the number of strings and `n` is the length of the longest string.
