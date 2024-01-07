class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # complexity nlogn
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 0
        best = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [x[0] for x in best[:k]]