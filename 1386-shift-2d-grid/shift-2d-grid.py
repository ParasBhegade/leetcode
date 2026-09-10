class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r=len(grid)
        c=len(grid[0])
        while k>0:
            last=grid[r-1][c-1]
            for i in range(r-1,-1,-1):
                for j in range(c-1,-1,-1):
                    if i == 0 and j == 0:
                        continue
                    elif j > 0:
                        grid[i][j] = grid[i][j-1]
                    else:
                        grid[i][0] = grid[i-1][j-1]
            grid[0][0]=last
            k-=1

        return grid