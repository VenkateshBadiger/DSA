class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse=int(str(abs(x))[::-1])
        return reverse==x
            
        
