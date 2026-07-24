import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        self.numArray = [-s for s in nums]

        heapq.heapify(self.numArray)

        for i in range(self.k - 1):
            heapq.heappop(self.numArray)

        return -self.numArray[0]
