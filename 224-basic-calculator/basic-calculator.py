class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        stack = []
        res = 0
        sign = 1
        num = 0
        i = 0
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num =0
                while i < len(s) and s[i].isdigit():
                    num = num*10 +int(s[i])
                    i += 1
                res += sign * num 
                continue

            elif ch == '+':
                sign = 1

            elif ch == '-':
                sign = -1

            elif ch == '(':
                stack.append((res,sign))
                res = 0
                sign = 1
                
            elif ch == ')':
                prev_res, prev_sign = stack.pop()
                res = prev_res + prev_sign*res

            i+=1
        return res


    '''
        def helper(i:int):    
            
            res = 0
            sign = 1
            num = 0
            
            while i < len(s):
                ch = s[i]

                if ch.isdigit():
                    num = num*10 +int(ch) 
                elif ch == '+':
                    res += sign * num
                    sign = 1
                    num = 0

                elif ch == '-':
                    res += sign * num
                    sign = -1
                    num = 0

                elif ch == '(':
                    inner_val, i = helper(i+1)
                    res += sign * inner_val 
                    num = 0

                elif ch == ')':
                    res += sign * num
                    return res, i
                i+=1
            res += sign * num 
            return res, i
        result, _ = helper(0)
        return result 
'''
