# Problem 329: Longest Increasing Path in a Matrix [1]
# [1]: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        
        visited = [[-1 for j in range(m)] for i in range(n)]
        ans     = [[1 for j in range(m)] for i in range(n)]
        
        maxi = 1

        def dfs(i, j):
            
            if visited[i][j] == 1:
                return ans[i][j]
            
            di = [(-1,0), (1,0), (0,-1), (0,1)]
            
            for x, y in di:
                xnew = i + x
                ynew = j + y
                if (0 <= xnew < n and 0 <= ynew < m and matrix[xnew][ynew] > matrix[i][j]):
                    ans[i][j] = max(ans[i][j], 1+dfs(xnew, ynew))
            
            visited[i][j] = 1

            return ans[i][j]
                
            
        for i in range(0, n):
            for j in range(0, m):
                ans[i][j] = dfs(i, j)
                maxi = max(maxi, ans[i][j])

        return maxi
