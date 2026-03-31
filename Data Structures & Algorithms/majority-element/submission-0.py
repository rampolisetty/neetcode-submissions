class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        major = len(nums)/2
        for idx, num in enumerate(nums):
            occur = track.get(num, 0)
            occur = occur + 1
            track[num] = occur
            if occur > major:
                return num
        return -1