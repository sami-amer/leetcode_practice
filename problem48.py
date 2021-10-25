class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # We can't create a new matrix, but we do at minimum need to hold a number or a row.
        
        matrix[:] = zip(*matrix[::-1])





if __name__ == "__main__":
    input1 = [[1,2,3],[4,5,6],[7,8,9]]
    # OUTPUT: [[7,4,1],[8,5,2],[9,6,3]]
    print(input1)