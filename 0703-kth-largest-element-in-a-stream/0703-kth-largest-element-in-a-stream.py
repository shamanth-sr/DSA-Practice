import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with kth largest number
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        # Checking if len(minHeap) > k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # if len(minHeap) < k, the nothing should be pop
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)