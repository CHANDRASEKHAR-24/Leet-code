class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        sol = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])-1, -1, -1):
                if grid[i][j] >= 0:
                    continue
                elif grid[i][j] < 0:
                    sol += 1
        return(sol)
        