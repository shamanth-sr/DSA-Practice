class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        count = {}

        for i in range(0, N):
            for j in range(0, N):
                if grid[i][j] not in count:
                    count[grid[i][j]] = 0
                count[grid[i][j]] += 1

        for num in range(1, N*N + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                repeat = num

        return [repeat, missing]