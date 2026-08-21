class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        #Options
        #l = 0 and r = 0 (add to list)
        #l = r (must take left)
        #l = 0 (must take right)
        #l < r (can take right or left)

        def rec(l, r):
            if l == 0 and r == 0:
                res.append("".join(temp))
            elif l == r:
                temp.append("(")
                rec(l - 1, r)
                temp.pop()
            elif l == 0:
                temp.append(")")
                rec(l, r - 1)
                temp.pop()
            else:
                temp.append("(")
                rec(l - 1, r)
                temp.pop()
                temp.append(")")
                rec(l, r - 1)
                temp.pop()
        rec(n, n)
        return res


