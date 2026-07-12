class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for st in strs:
            while len(prefix)>0:
                if st.startswith(prefix):
                    break
                else:
                    prefix = prefix[0:-1]
        return prefix          
