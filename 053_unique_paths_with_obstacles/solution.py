import typing


class Solution:
    def unique_paths_with_obstacles(self, obstacle_grid: typing.List[typing.List[int]]) -> int:

        num_rows = len(obstacle_grid)
        num_cols = len(obstacle_grid[0])
        paths_grid = [[0] * num_cols for _ in range(num_rows)]

        # fill in the first row...
        for c in range(num_cols):
            if obstacle_grid[0][c] == 0:
                paths_grid[0][c] = 1
            else:
                break

        # ...and the first column
        for r in range(num_rows):
            if obstacle_grid[r][0] == 0:
                paths_grid[r][0] = 1
            else:
                break

        # fill in the rest of the grid
        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if obstacle_grid[r][c] == 1:
                    paths_grid[r][c] == 0
                else:
                    paths_grid[r][c] = paths_grid[r - 1][c] + paths_grid[r][c - 1]

        return paths_grid[num_rows - 1][num_cols - 1]


if __name__ == "__main__":
    s = Solution()

    assert s.unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.unique_paths_with_obstacles([[0, 1], [0, 0]]) == 1

    print("Simple test cases passed!")
