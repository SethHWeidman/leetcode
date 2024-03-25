import typing


class Solution(object):
    def length_of_LIS(self, nums: typing.List[int]) -> int:
        # a "dynamic programming" solution:
        # `dp` will store the longest increasing subsequence ending at [i]
        dp = [1] * len(nums)
        for j in range(len(nums)):
            # iterate through the prior elements of `nums`
            # for each prior element, assuming `dp[i]` is correct, then if `nums[j] > nums[i]`,
            # index `j` produces a subsequence with length `dp[i] + 1`
            for i in range(0, j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


if __name__ == "__main__":
    s = Solution()

    assert s.length_of_LIS([4, 10, 4, 8, 9]) == 3
    assert s.length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    print("Simple test cases passed!")
