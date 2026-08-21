class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.getNumber(num1)
        n2 = self.getNumber(num2)

        num = n1 * n2
        if num == 0:
            return "0"
        res = ""
        while num > 0:
            mod = num % 10
            num = num // 10
            res = str(mod) + res
        return res

    def getNumber(self, strnum):
        res = 0
        size = 10 ** (len(strnum) - 1)
        for c in strnum:
            val = ord(c) - ord("0")
            res += size * val
            size = size // 10
        return res
                 