class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longest):
                    longest = s[i:j]
        return longest 
