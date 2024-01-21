class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mem = {}
        for w in words:
            mem[w] = mem.get(w,0) + 1
        h = []
        for x in mem.items():
            w, cnt = x
            heapq.heappush(h, ((-cnt,w), w))
        # k logn
        return [x[1] for x in [heapq.heappop(h) for _ in range(k)]]