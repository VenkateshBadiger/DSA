class Solution:
    def reverse(self, x: int) -> int:
        
        reverse_num=int(str(abs(x))[::-1])
        if x<0:
            reverse_num = -reverse_num
        #return reverse_num
        if -2**31<= reverse_num <=2**31:
            return reverse_num
        else:
            return 0

        '''
        reverse_num= 0
        while n>0:
            digit = n % 10
            reverse_num= reverse_num*10 + digit
        if x<0:
            reverse_num = -reverse_num
        return reverse_num
        '''