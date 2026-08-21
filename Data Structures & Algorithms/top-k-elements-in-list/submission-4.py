class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use an array of len(nums) with a hashmap for knowing the index
        # Once done, get k most freq from array

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freqarr = [[] for _ in range(len(nums) + 1)]
        for key in freq:
            freqarr[freq[key]].append(key)
        
        res = []
        i = len(nums)
        while len(res) < k:
            res.extend(freqarr[i])
            i -= 1
        return res