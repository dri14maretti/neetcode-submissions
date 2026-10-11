class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = 9,9
        def resolveGrid(i, j):
            rowsRes = i // 3
            colsRes = j // 3 + 1

            print(i, j, rowsRes * 3 + colsRes)

            return rowsRes * 3 + colsRes

        colsSet = set()
        rowsSet = set()
        gridSet = set()

        for i in range(rows):
            for j in range(cols):
                element = board[i][j]
                grid = resolveGrid(i, j)
                if element == '.':
                    continue
                    
                if ((i, element) in rowsSet
                or (j, element) in colsSet
                or (grid, element) in gridSet):
                    return False
                
                rowsSet.add((i, element))
                colsSet.add((j, element))
                gridSet.add((grid, element))

        return True
