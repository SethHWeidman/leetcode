import typing


class Solution:
    def minimum_path_sum(self, grid: typing.List[typing.List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        minimum_sums = [[-1] * n_cols for _ in range(n_rows)]
        minimum_sums[0][0] = grid[0][0]

        for col in range(1, n_cols):
            minimum_sums[0][col] = minimum_sums[0][col - 1] + grid[0][col]

        for row in range(1, n_rows):
            minimum_sums[row][0] = minimum_sums[row - 1][0] + grid[row][0]

        for row in range(1, n_rows):
            for col in range(1, n_cols):
                minimum_sums[row][col] = (
                    min(minimum_sums[row - 1][col], minimum_sums[row][col - 1]) + grid[row][col]
                )

        return minimum_sums[n_rows - 1][n_cols - 1]


if __name__ == "__main__":
    s = Solution()

    s.minimum_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7

    print("Simple test cases pass!")
