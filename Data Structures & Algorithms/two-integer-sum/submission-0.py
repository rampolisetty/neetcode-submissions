class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res_list = []
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in seen:
                res_list = [seen[other_num], idx]
                break
            else:
                seen[num] = idx
        return res_list