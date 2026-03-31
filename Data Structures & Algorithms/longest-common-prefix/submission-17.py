class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        for idx, ch in enumerate(strs[0]):
            print(idx, ch)
            for s in strs:
                if idx == len(s):
                    return res
                if ch != s[idx]:
                    return res
            res += ch
        return res