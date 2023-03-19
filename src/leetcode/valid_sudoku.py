# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r = self.check_row(board, i)
            c = self.check_column(board, i)
            b = self.check_box(board, i)
            if not r & c & b:
                return False
        return True
            
    def check_row(self, board, i):
        nums = [0] * 9
        for j in board[i]:
            if j != '.':
                nums[int(j)-1] += 1
        if max(nums) > 1:
            return False
        return True
    
    def check_column(self, board, i):
        nums = [0] * 9
        for j in range(9):
            elem = board[j][i]
            if elem != '.':
                nums[int(elem)-1] += 1
        if max(nums) > 1:
            return False
        return True
    
    def check_box(self, board, i):
        nums = [0] * 9
        row_start = i // 3 * 3
        column_start = i % 3 * 3
        for i in range(row_start, row_start+3):
            for j in range(column_start, column_start + 3):
                elem = board[i][j]
                if elem != '.':
                    nums[int(elem)-1] += 1
        if max(nums) > 1:
            return False
        return True
