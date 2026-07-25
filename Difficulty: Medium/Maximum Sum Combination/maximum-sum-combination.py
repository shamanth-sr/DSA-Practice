import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        
        # Reverse Sort arrays
        a.sort(reverse = True)
        b.sort(reverse = True)
        
        # Initial max-heap
        max_heap = [(-(a[0] + b[0]), 0, 0)]
        
        # To track of visited index pairs
        visited = set()
        visited.add((0, 0))
        
        # result list
        result = []
        
        # run loop for k times
        for _ in range(k):
            # extract max sum combo
            sum_neg, i, j = heapq.heappop(max_heap)
            
            # convert sum value back
            result.append(-sum_neg)
            
            # push i+1 element from 'a' if not visited
            if i+1 < len(a) and (i+1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i+1] + b[j]), i+1, j))
                visited.add((i+1, j))
                
            if j+1 < len(b) and (i, j+1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j+1]), i, j+1))
                visited.add((i, j+1))
                
        return result
        
        
        