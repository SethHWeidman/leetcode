import typing


class Solution:
    def maximum_sum_circular_subarray(self, nums: typing.List[int]) -> int:
        total = 0
        cur_max = 0
        max_sum = float("-inf")
        cur_min = 0
        min_sum = float("inf")

        for num in nums:

            # after each iteration, we want:
            #   * `cur_max` to be the sum of the largest subarray ending with `num`; either
            #     * `cur_max + num` is greater than `cur_max` OR
            #     * `cur_max` is negative and thus `num` is greater than `cur_max + num`
            cur_max = max(cur_max + num, num)
            # we update `max_sum` to be the maximum `cur_max` we've seen so far
            max_sum = max(max_sum, cur_max)

            # we update `cur_min` and `min_sum` similarly
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            total += num

        # finally, we check if a "circular" sum is greater than `max_sum` in the following clever
        # way: we compare it to `total - min_sum`!
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


if __name__ == "__main__":
    s = Solution()

    assert s.maximum_sum_circular_subarray([1, -2, 3, -2]) == 3
    assert s.maximum_sum_circular_subarray([5, -3, 5]) == 10
    assert s.maximum_sum_circular_subarray([-3, -2, -3]) == -2

    print("Simple test cases passed!")
