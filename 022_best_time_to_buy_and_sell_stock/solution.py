import typing


class Solution:
    def max_profit(self, prices: typing.List[int]) -> int:
        # we need to keep track of two elements: the `minimum` - because this element provides the
        # most "potential for profit" - and the actual `max_profit`
        minimum = float("inf")
        max_profit = 0

        for price in prices:
            if price < minimum:
                minimum = price

            candidate_max_profit = price - minimum
            if candidate_max_profit > max_profit:
                max_profit = candidate_max_profit

        return max_profit


if __name__ == "__main__":
    s = Solution()

    assert s.max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert s.max_profit([7, 6, 4, 3, 1]) == 0

    print("Simple test cases passed!")
