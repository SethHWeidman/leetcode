import typing


class Solution:
    def plus_one(self, digits: typing.List[int]) -> typing.List[int]:

        N = len(digits)
        for i in range(N - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    s = Solution()

    assert s.plus_one([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plus_one([3, 6, 9, 9]) == [3, 7, 0, 0]
    assert s.plus_one([3, 6, 9]) == [3, 7, 0]
    assert s.plus_one([1, 2, 3]) == [1, 2, 4]
    assert s.plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]

    print("Test cases passed!")
