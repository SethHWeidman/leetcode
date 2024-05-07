import typing


class Solution:
    def coin_change(self, coins: typing.List[int], amount: int) -> int:
        # nums_coins will hold, for i = 0 to `amount`, the minimum number of coins it takes to
        # reach `amount`
        nums_coins = [float("inf")] * (amount + 1)
        nums_coins[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                nums_coins[i] = min(nums_coins[i], nums_coins[i - coin] + 1)

        return nums_coins[amount] if nums_coins[amount] < float("inf") else -1


if __name__ == "__main__":
    s = Solution()

    assert s.coin_change([1, 2, 5], 11) == 3
    assert s.coin_change([2], 3) == -1
    assert s.coin_change([1], 0) == 0

    print("Simple test cases passed!")
