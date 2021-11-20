from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()

        n = len(matrix[0]) # length of row
        m = len(matrix)# length of columns

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    cols.add(x)
                    rows.add(y)

        # for y in range(m):
        #     for x in range(n):
        #         if y in rows:
        #             matrix[y] = [0 for _ in matrix[y]]
        #         if x in cols:
        #             matrix[y][x] = 0

        for r in rows:
            matrix[r] = [0] * n
        for c in cols:
            for row in matrix:
                row[c] = 0
                





if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # Output = [[1,0,1],[0,0,0],[1,0,1]]
    # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # Output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    Solution.setZeroes(None,matrix)
    print(matrix)