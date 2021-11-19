class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_path = [[1 for x in range(n)] for y in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp_path[i][j] = dp_path[i-1][j] + dp_path[i][j-1]
        
        return dp_path[m-1][n-1]



if __name__ == '__main__':
    m = 3
    n = 7
    # Output = 28
    print(Solution.uniquePaths(None,m,n))
