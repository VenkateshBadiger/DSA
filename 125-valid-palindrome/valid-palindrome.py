class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(filter(str.isalnum, s)).lower()
        p= str(s)[::-1]
        return p==s 