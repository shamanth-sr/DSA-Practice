class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # target = 10

        ROWS = len(matrix)              # 3
        COLS = len(matrix[0])           # 4

        l, r = 0, ROWS * COLS -1        # (0, 11)
        
        while l <= r:
            mid = l + ((r - l) // 2)    # 5, 6

            row = mid // COLS           # 1, 1
            col = mid % COLS            # 1, 2

            if target < matrix[row][col]:   # 10 !< 13
                r = mid - 1                 # 1

            elif target > matrix[row][col]:     
                l = mid + 1

            else:
                return True

        return False
