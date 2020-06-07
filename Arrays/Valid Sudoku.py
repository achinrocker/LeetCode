class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 9] * 9
        col = [[0] * 9] * 9

        for i in range(0, 3):
            for j in range(0, 3):
                box = [0] * 9
                for k in range(0, 3):
                    for l in range(0, 3):
                        if board[k + i * 3][l + j * 3] == ".":
                            continue
                        else:
                            print("x = " + str(i * 3 + k) + "y = " + str(l + j * 3))
                            row[i * 3 + k][int(board[k + i * 3][l + j * 3])] += 1
                            col[j * 3 + l][int(board[k + i * 3][l + j * 3])] += 1
                            box[int(board[k + i * 3][l + j * 3])] += 1
                # check box
                for item in box:
                    if item > 1:
                        return False

        for i in range(0, 9):
            for item_r, item_c in row[i], col[i]:
                if item_r > 1 or item_c > 1:
                    return False

        return True