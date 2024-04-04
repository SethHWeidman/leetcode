class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # simple dynamic programming solution
        dp = n * [0]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n - 1]


if __name__ == "__main__":

    s = Solution()

    assert s.climb_stairs(1) == 1
    assert s.climb_stairs(3) == 3

    print("Simple test cases passed!")
