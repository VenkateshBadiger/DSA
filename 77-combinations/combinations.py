class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            if start >n:
                return 
            path.append(start)
            backtrack(start+1, path)
            path.pop()

            backtrack(start+1, path)
        backtrack(1,[])
        return res