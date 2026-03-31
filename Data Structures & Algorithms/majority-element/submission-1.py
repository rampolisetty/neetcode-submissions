class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # Every time you "cancel out" one majority element with a non-majority element, you're removing 2 elements
        # Even if ALL non-majority elements cancel with majority elements, the majority will still have leftover votes
        # The final candidate MUST be the majority element
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1 # +1
                continue
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

