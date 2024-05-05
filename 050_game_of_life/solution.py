import typing


class Solution:
    def game_of_life(self, board: typing.List) -> typing.List:
        num_rows = len(board)
        num_cols = len(board[0])

        # idea:
        #   * if a cell is newly dead, initially set the value to -1
        #   * then, when checking for neighbors that are alive, we can check if the value of the
        #     neighboring cells are equal to 1 or -1
        #   * if a cell is newly alive, initially set the value to 2
        #   * correct values to be only 0 and 1
        for r in range(num_rows):
            for c in range(num_cols):
                num_neighbors = self._get_num_neighbors(board, num_rows, num_cols, r, c)

                # rules 1 and 3
                if board[r][c] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                    board[r][c] = -1

                # rule 4
                if board[r][c] == 0 and num_neighbors == 3:
                    board[r][c] = 2

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] <= 0:
                    board[r][c] = 0
                else:
                    board[r][c] = 1

        return board

    def _get_num_neighbors(
        self, board: typing.List, max_rows: int, max_cols: int, r: int, c: int
    ) -> int:
        cnt = 0
        neighbor_indices = [-1, 0, 1]
        for i in neighbor_indices:
            new_row_index = r + i
            if new_row_index < 0 or new_row_index >= max_rows:
                continue
            for j in neighbor_indices:
                new_col_index = c + j
                if new_col_index < 0 or new_col_index >= max_cols:
                    continue

                if i == 0 and j == 0:
                    continue

                new_value = board[new_row_index][new_col_index]
                if new_value == 1 or new_value == -1:
                    cnt += 1
        return cnt


if __name__ == "__main__":
    s = Solution()

    assert s.game_of_life([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]) == [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0],
    ]
    assert s.game_of_life([[1, 1], [1, 0]]) == [[1, 1], [1, 1]]

    print("Simple test cases passed!")
