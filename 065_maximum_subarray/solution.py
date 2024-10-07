import typing


class Solution:
    def max_sub_array(self, nums: typing.List[int]) -> int:
        max_sum = float("-inf")
        cur_max = float("-inf")

        for num in nums:
            max_sum = max(max_sum + num, num)
            if max_sum > cur_max:
                cur_max = max_sum

        return cur_max


if __name__ == "__main__":
    s = Solution()

    assert s.max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.max_sub_array([1]) == 1
    assert s.max_sub_array([5, 4, -1, 7, 8]) == 23

    print("Simple test cases passed!")
