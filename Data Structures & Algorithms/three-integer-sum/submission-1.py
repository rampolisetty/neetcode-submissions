class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out_list = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1 # O(1), so no issues
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    out_list.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1


        return out_list     