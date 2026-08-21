class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        res = []
        for value in m:
            res.append((m[value], value))
        
        res.sort(reverse=True)

        final = []

        for i in range(k):
            final.append(res[i][1])
        return final
