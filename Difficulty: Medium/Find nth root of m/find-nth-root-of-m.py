class Solution:
    def nthRoot(self, n, m):
       # code here
        left, right = 0, m
       
        while left <= right:
            mid = left + ((right - left) // 2)
            
            if mid ** n == m:
               return mid
            
            elif mid ** n > m:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return right if right ** n == m else -1

