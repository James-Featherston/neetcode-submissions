class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        # Store frequency of each number (hashmap?)

        # Find the k lowest frequencies (sort), maybe with tuple
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = []
        for key in freq:
            res.append((freq[key], key))

        res.sort(reverse=True)

        res1 = []
        for i in range(k):
            res1.append(res[i][1])
        return res1