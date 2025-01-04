import typing


class Solution:
    def jumps(self, nums: typing.List[int]) -> int:
        if len(nums) == 1:
            return 0

        current_furthest = 0
        next_furthest = 0
        num_jumps = 0

        for i in range(len(nums) - 1):
            next_furthest = max(next_furthest, i + nums[i])

            if i == current_furthest:
                num_jumps += 1
                current_furthest = next_furthest

                if current_furthest >= len(nums) - 1:
                    return num_jumps

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.jumps([0]) == 0
    assert s.jumps([2, 3, 1, 1, 4]) == 2

    print("All test cases passed!")
