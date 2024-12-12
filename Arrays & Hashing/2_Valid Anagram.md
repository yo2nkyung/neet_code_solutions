# 2. Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

```
Input: s = "racecar", t = "carrace"
Output: true
```
Example 2:
```
Input: s = "jar", t = "jam"
Output: false
```
Constraints:

s and t consist of lowercase English letters.

## Solution
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
```
For each character in `s` and `t`:
- Increment the count for the character in `s`.
- Decrement the count for the character in `t`.

The `ord()` function converts a character into its ASCII value:
- `ord('a')` is 97, so `ord(s[i]) - ord('a')` maps 'a' to index 0, 'b' to index 1, and so on.

## Result
Time & Space Complexity
- Time complexity: O(n+m)
- Space complexity: O(1) since we have at most 26 different characters.
> Where n is the length of string s and m is the length of string t.
