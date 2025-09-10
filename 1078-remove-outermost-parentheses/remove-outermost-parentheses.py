class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        new = ""
        for ch in s:
            if ch == "(":
                if counter > 0:
                    new = new + ch 
                counter = counter + 1
                
            elif ch == ")":
                counter = counter - 1
                if counter > 0:
                    new = new + ch
        return new