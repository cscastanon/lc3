#LeetCode Problem 3
#Info: Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def longestSubstring(self, s:str) -> int:
        subStringSet =  set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in subStringSet:
                subStringSet.remove(s[l])
                l += 1
            
            subStringSet.add(s[r])
            result = max(result, r-l + 1)
        return result