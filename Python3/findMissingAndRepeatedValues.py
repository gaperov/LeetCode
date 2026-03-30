class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = set()
        ch_mis = set(range(1, len(grid)**2+1))
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in repeated:
                    ans.append(grid[i][j])
                repeated.add(grid[i][j])
        return ans + list(ch_mis - repeated)
