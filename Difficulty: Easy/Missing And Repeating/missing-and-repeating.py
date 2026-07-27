class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        
        count = {}
        
        for i in range(n):
            if arr[i] not in count:
                count[arr[i]] = 0
            count[arr[i]] += 1
            
        for num in range(0, n + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                repeat = num
                
        return [repeat, missing]

