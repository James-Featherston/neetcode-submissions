class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mult = 2 ** 31

        while n != 0:
            cur = n % 2
            n = n // 2
            res = res + (mult * cur)
            mult = mult // 2
        return res
