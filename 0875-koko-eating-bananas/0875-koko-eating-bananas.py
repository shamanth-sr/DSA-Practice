class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            mid = l + ((r-l)//2)

            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(p/ mid) 

            if timeTaken <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res