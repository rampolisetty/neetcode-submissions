class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        for idx, ch in enumerate(strs[0]):
            for s in strs:
                if idx == len(s) or s[idx] != ch:
                    return res
            res += ch
        
        return res