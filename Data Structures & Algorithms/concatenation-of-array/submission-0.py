class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for idx, val in enumerate(nums):
            ans.append(val)
      
        for idx, val in enumerate(nums):
            ans.append(val)
        
        return ans
        # Pythonic way
        # return nums + nums
