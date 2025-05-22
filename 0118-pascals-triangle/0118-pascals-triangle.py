class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        triangle = self.generate(numRows - 1)
        last_row = triangle[-1]
        new_row = [1]  # start with 1
        
        # compute the middle values
        for i in range(1, numRows - 1):
            new_row.append(last_row[i - 1] + last_row[i])
        new_row.append(1)  # end with 1
        
        triangle.append(new_row)
        return triangle