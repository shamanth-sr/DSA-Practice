class Solution:
    def kthElement(self, a, b, k):
        # code here
        last, i, j = 0, 0, 0
        
        n = len(a)
        m = len(b)
        
        for _ in range(k):
            if i < n:
                if j < m and a[i] > b[j]:
                    last = b[j]
                    j += 1
                else:
                    last = a[i]
                    i += 1
                    
            elif j < m:
                last = b[j]
                j += 1
                
        return last