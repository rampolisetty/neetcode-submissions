class Solution:
    def reverseBits(self, n: int) -> int:
        # measure bit length first
        bit_len = 0
        tmp = n
        while tmp > 0:
            bit_len += 1
            tmp = tmp >> 1
        
        # Perform reverse
        res = 0
        for idx in range(bit_len):
            bit = (n >> idx) & 1
            res |= (bit << (31 - idx))
        return res