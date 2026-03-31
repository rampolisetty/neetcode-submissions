class Solution:
    # Time O(n^2)
    # Space O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, one in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                idx += 1
                continue
            
            # Optimization, once we reach +ve, can't find a triplet which can sum to 0
            if one > 0:
                break

            # 2 Sums
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                three_sum = one + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([one, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Avoid duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        continue
        return res
