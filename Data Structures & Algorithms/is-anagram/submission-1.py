class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_dict = {}
        for c in s:
            res_dict[c] = res_dict.get(c, 0) + 1
        
        for c in t:
            if c not in res_dict:
                return False
            res_dict[c] -= 1
            if res_dict[c] == 0:
                res_dict.pop(c)
            
        return not res_dict
