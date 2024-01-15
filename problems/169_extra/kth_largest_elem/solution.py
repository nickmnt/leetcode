class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1
        return -heapq.heappop(nums)