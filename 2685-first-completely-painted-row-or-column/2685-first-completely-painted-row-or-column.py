class Solution:
    def firstCompleteIndex(self, arr, mat):
        m = len(mat)
        n = len(mat[0])
        
        # Map value to cell coordinates
        value_to_index = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}

        # Count painted cells in each row and column
        row_paint_count = [0] * m
        col_paint_count = [0] * n

        for i, val in enumerate(arr):
            row, col = value_to_index[val]

            # Increment painted cell counts for row and column
            row_paint_count[row] += 1
            col_paint_count[col] += 1

            # Check if row or column is completely painted
            if row_paint_count[row] == n or col_paint_count[col] == m:
                return i

        return -1
