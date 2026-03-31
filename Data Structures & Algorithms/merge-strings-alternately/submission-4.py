class Solution:
    # Time O(n + m) and Space O(n + m)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l1 = len(word1)
        l2 = len(word2)
        l1_idx = l2_idx = 0
        while l1_idx < l1 or l2_idx < l2:
            if l1_idx < l1:
                res.append(word1[l1_idx])
                l1_idx += 1
            if l2_idx < l2:
                res.append(word2[l2_idx])
                l2_idx += 1
        return "".join(res)