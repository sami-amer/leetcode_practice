class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # We can't create a new matrix, but we do at minimum need to hold a number or a row.
        
        # matrix[:] = zip(*matrix[::-1])
        n = len(matrix)

        matrix.reverse()
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]





if __name__ == "__main__":
    input1 = [[1,2,3],[4,5,6],[7,8,9]]
    # OUTPUT: [[7,4,1],[8,5,2],[9,6,3]]
    Solution.rotate(None,input1)
    print(input1)