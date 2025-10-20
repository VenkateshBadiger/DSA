from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        parts = path.split('/')
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                        stack.pop()
            else:
                stack.append(part)
        res = ""
        while stack:
            res = "/" + stack.pop() + res    

        return res if res else '/'        