from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening  = [ "(" , "{" , "[" ]
        match = {')': '(', '}' : '{' , ']' : '['}

        for ch in s:
            if ch in opening:
                stack.append(ch)
            elif ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
        return not stack