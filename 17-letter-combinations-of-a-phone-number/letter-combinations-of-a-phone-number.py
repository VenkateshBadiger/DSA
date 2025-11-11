keys = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

def combinations(inpt):
    if inpt == '':      #base case
        return ['']
    ans = []
    words = keys[inpt[0]]
    small_inpt = combinations(inpt[1:])
    
    for word in words:
        for inpt in small_inpt:
            ans.append(word + inpt)

    return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        return combinations(digits)