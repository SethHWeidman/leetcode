import typing


class Solution:
    def find_min_arrow_shots(self, points: typing.List[typing.List[int]]) -> int:

        points.sort(key=lambda x: x[1])

        num_arrows = 0
        current_pos = float("-inf")
        for point_min, point_max in points:
            if current_pos < point_min:
                current_pos = point_max
                num_arrows += 1

        return num_arrows


if __name__ == "__main__":
    s = Solution()

    assert s.find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert s.find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert s.find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2

    print("Simple test cases passed!")
