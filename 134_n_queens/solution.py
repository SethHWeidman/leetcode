import typing


class Solution:
    def total_n_queens(self, n: int) -> int:
        # https://en.wikipedia.org/wiki/Eight_queens_puzzle
        # Beautiful use of the backtracking method: https://en.wikipedia.org/wiki/Backtracking
        def backtrack(
            row: int, columns: typing.Set, diagonals: typing.Set, anti_diagonals: typing.Set
        ) -> int:
            if row == n:
                return 1

            tot = 0
            for column in range(n):
                diagonal = row - column
                anti_diagonal = row + column
                if column in columns or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue

                columns.add(column)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)

                tot += backtrack(row + 1, columns, diagonals, anti_diagonals)

                columns.remove(column)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

            return tot

        return backtrack(0, set(), set(), set())


if __name__ == "__main__":
    s = Solution()

    assert s.total_n_queens(4) == 2
    assert s.total_n_queens(5) == 10
    assert s.total_n_queens(6) == 4

    print("Test cases passed!")
