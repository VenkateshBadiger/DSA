class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        print(lst)
        string = lst[::-1]
        final = string.pop(0)
        while len(string) >0:
            final = final + " " + string.pop(0)
        return final