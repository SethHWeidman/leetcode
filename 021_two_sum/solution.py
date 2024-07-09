import typing


class Solution:
    def two_sum(self, nums: typing.List[int], target: int) -> typing.List[int]:

        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i, num in enumerate(nums):
            other = target - num
            if other in nums_dict and nums_dict[other] != i:
                return [i, nums_dict[other]]


if __name__ == "__main__":
    s = Solution()

    assert s.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert s.two_sum([3, 2, 4], 6) == [1, 2]
    assert s.two_sum([3, 3], 6) == [0, 1]
