class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        arr = []
        while x != 0:
            arr.append(x % 10)
            x = x // 10
        mult = 10 ** (len(arr) - 1)
        res = 0
        for num in arr:
            res += num * mult
            mult = mult // 10
        res = res * sign
        if res < -1 * (2 ** 31) or res >= 2 ** 31:
            return 0
        return res
        