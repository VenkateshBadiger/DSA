class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        join_reverse= " ".join(words)
        return join_reverse