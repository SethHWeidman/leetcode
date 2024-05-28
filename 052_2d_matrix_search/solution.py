import typing


class Solution:
    def search_matrix(
        self, matrix: typing.Optional[typing.List[typing.List[int]]], target: int
    ) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        total_elements = num_rows * num_cols

        low = 0
        high = total_elements - 1

        # binary search
        while low <= high:
            mid = (low + high) // 2

            row = mid // num_cols
            col = mid % num_cols
            element = matrix[row][col]

            if element == target:
                return True
            elif element > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


if __name__ == "__main__":

    s = Solution()

    assert s.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1)
    assert s.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60)

    assert not s.search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)

    assert s.search_matrix([[1]], 1)
    assert s.search_matrix([[1, 3]], 3)

    print("Simple test cases passed!")
