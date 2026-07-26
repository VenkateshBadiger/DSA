class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
# string.find(substring)
        index = haystack.find(needle)
        return index