class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Go through each word, find it's breakdown, add to hashmap
        hmap = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord("a")] += 1
            hmap[tuple(arr)].append(word)
        return list(hmap.values())
        
        

        # Go through keys, add to final result