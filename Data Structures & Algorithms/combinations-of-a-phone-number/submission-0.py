class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        res = []
        temp = []

        def rec (rem):
            if not rem:
                res.append("".join(temp))
                return
            digit = rem[0]
            rem = rem[1:]
            for c in m[digit]:
                temp.append(c)
                rec(rem)
                temp.pop()
        if digits:
            rec (digits)
        return res
        