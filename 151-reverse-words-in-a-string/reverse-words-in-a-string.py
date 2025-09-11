class Solution:
    def reverseWords(self, s: str) -> str:
        list_s_rev = s.split()[::-1]
        rev = " ".join(list_s_rev)
        return rev