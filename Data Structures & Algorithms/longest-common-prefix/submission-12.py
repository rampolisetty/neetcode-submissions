class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        for i, ch in enumerate(strs[0]):
            for s in strs:
                if i == len(s) or s[i] != ch:
                    return res
            res += ch
        return res