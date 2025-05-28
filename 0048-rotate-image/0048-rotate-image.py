class Solution(object):
    def rotate(self, matrix):
        # a=len(matrix)
        # b=len(matrix[0])
        # arr_matrix=[[0]*a for _ in range(b)]
         
        # for i in range (a):
        #     for j in range (b):
        #         arr_matrix[j][a-i-1]=matrix[i][j]
        # return arr_matrix

        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix
        