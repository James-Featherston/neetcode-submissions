class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        comb = []
        for i in range(len(speed)):
            comb.append((position[i], speed[i]))
        comb.sort()
        
        steps = [0] * len(comb)

        for i in range(len(comb)):
            s = (target - comb[i][0]) / comb[i][1]
            steps[i] = s
        
        res = 1
        cur = steps.pop()
        while steps:
            if cur >= steps[-1]:
                steps.pop()
            else:
                cur = steps.pop()
                res += 1
        return res
            

        

        

        