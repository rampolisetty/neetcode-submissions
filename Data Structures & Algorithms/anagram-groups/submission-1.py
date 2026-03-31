class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #Map char_count to a list of anagrams

        for s in strs:
            char_count = [0] * 26 # 26 lower case alphabets
            for c in s:
                # [1, 0, 1, . . . . 0]
                # [a, b, c, d, . . . z]
                char_count[ord(c) - ord("a")] += 1
            res[tuple(char_count)].append(s)
        print(res.values())
        return list(res.values())