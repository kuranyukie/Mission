# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-sudoku/

board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]

from typing import List

class Solution:
    def isValidSudoku2(self, board: List[List[str]]) -> bool: #解法2
        f1 = lambda _ : (__ for __ in _ if __ != '.')
        f2 = lambda _ : len(set(f1(_))) == len(list(f1(_)))
        return all(
            all(map(f2, board)),
            all(map(f2, [[board[j][i] for j in range(9)] for i in range(9)])),
            all(map(f2, [
                [ board[(i // 3) * 3][(i % 3) * 3 + j] for j in range(3)] +
                [ board[(i // 3) * 3 + 1][(i % 3) * 3 + j] for j in range(3) ] +
                [ board[(i // 3) * 3 + 2][(i % 3) * 3 + j] for j in range(3) ]
                for i in range(9)
            ]))
        )

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board += self.generateCols(board)
        board += self.generateSubBox(board)
        for lst in board :
            if not self.isValidList(lst) :
                print("=========================This list is False")
                return False
            else : print("========================This list is True")

        print("==============================The whole sudoku is True")
        return True
    
    def generateCols(self, board: List[List[str]]) -> List[List[str]]:
        cols = []
        for i in range(9) :
            aCol = []
            for j in range(9) :
                aCol.append(board[j][i])
            cols.append(aCol)
        return cols

    def generateSubBox(self, board: List[List[str]]) -> List[List[str]]:
        subBoxDict = {} # {(0,0): ["5", "3", "." ...]}
        for i in range(9):
            # print(f'{i = }')
            for j in range(9):
                # print(f'{j = }')
                if (i//3, j//3) not in subBoxDict:
                    # print(f'{i//3 = }')
                    # print(f'{j//3 = }')
                    # print(f'{board[i][j] = }')
                    # print("add a new key")
                    subBoxDict[(i//3, j//3)] = []
                subBoxDict[(i//3, j//3)].append(board[i][j])
        # print(f'{subBoxDict = }')
        # print(list(subBoxDict.values()))
        return list(subBoxDict.values())

    def isValidList(self, lst: List[str]) -> bool:
        nums = []
        for i in range(9) :
            # print(f'{i = }')
            if lst[i] != "." :
                # print(f'{lst[i] = }')
                if lst[i] not in nums :
                    nums.append(lst[i])
                    # print(f'{nums = }')
                else : return False
        return True
