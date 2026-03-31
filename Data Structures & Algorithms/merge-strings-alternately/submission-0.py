class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        idx = 0
        res = []
        l1_idx = l2_idx = 0
        while idx < l1 + l2:
            if l1_idx < l1:
                res.append(word1[l1_idx])
                idx += 1
                l1_idx += 1
            if l2_idx < l2:
                res.append(word2[l2_idx])
                idx += 1
                l2_idx += 1

        return "".join(res)