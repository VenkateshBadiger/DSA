class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
# With n-m+1 we are kinda not considering the last m characters as when we reach n-m th character we compare them already 
        if needle not in haystack:
            return -1
        elif needle: 
            n = len(haystack)
            m = len(needle)
            for i in range(n- m + 1):
                if haystack[i] == needle[0] and haystack[i:i+m]== needle:
                    return i
                    