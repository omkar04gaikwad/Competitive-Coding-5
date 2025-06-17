###
# Approach:
# - Use three arrays of sets: one for each row, column, and 3x3 box.
# - For each cell, if it's a digit (not '.'), check:
#     - if it already exists in the same row, column, or box → return False
#     - otherwise, add it to the respective row, column, and box sets
# - If we go through the entire board without duplicates → return True
#
# Time Complexity: O(1) — fixed 9x9 board
# Space Complexity: O(1) — fixed 9 sets for rows, columns, and boxes
###
class Solution:
    def isValid(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    box_idx = (i//3)*3 + (j//3)
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[box_idx]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[box_idx].add(board[i][j])
        return True
    
    def main(self):
        # Valid Sudoku Example
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        result = self.isValid(board)
        print("Is board valid?", result)  # Expected: True

# Run the main function
sol = Solution()
sol.main()