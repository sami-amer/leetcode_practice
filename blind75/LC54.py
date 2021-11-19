from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Idea 1: add items and DELETE THEM
        # add first row, delete it
        # go through and add last element of every row, delete them when added
        # when on last row add entire row in reverse order, delete it
        # Start Again

        res = []

        while matrix:
            res += matrix[0]
            matrix.pop(0)
            if not any(matrix):
                return res
            for row in matrix:
                res.append(row[-1])
                row.pop(-1)
            res += matrix[-1][::-1]
            matrix.pop(-1)
            if not any(matrix):
                return res
            for row in matrix[::-1]:
                res.append(row[0])
                row.pop(0)
        return res






if __name__ == '__main__':
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # output = [1,2,3,6,9,8,7,4,5]
    # matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    print(Solution.spiralOrder(None,matrix))


        # while matrix:
        #     res+=(matrix[0]) # add first row
        #     matrix.pop(0) # then remove it
        #     num_rows = len(matrix)
        #     for i, row in enumerate(matrix):
        #         if not row:
        #             continue
        #         if i == num_rows - 1:
        #             res+=(row[::-1])
        #             matrix.pop(i)
        #             for j, row in enumerate(matrix[::-1]):
        #                 if j == num_rows - 2:
        #                     break
        #                 res.append(row[0])
        #                 row.pop(0)
        #         else:
        #             res.append(row[-1])
        #             row.pop(-1)
        # return(res)