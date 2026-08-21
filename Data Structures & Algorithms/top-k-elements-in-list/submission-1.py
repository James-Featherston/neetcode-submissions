class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        buckets = [[] for _ in range(len(nums))]

        for value in m:
            buckets[m[value] - 1].append(value)
        
        res = []

        for i in range (len(nums) - 1, -1, -1):
            for val in buckets[i]:
                res.append(val)
        
        
        return res[0 : k]
