import typing


class Solution:
    def minimum_total(self, triangle: typing.List[typing.List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for column in range(len(triangle[row])):
                triangle[row][column] += min(
                    triangle[row + 1][column], triangle[row + 1][column + 1]
                )
        return triangle[0][0]


if __name__ == "__main__":
    s = Solution()

    assert s.minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert s.minimum_total([[-10]]) == -10

    print("Simple test cases passed!")
