class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_count = []
        for num in range(n + 1):
            count = 0
            while num > 0:
                if num & 1:
                    count += 1
                num = num >> 1
            bit_count.append(count)
        return bit_count