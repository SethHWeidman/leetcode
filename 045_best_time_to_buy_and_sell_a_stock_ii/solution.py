import typing


class Solution(object):
    def max_profit(self, s: typing.List[int]) -> int:
        # it turns out, the algorithm can simply be: if the price went up the day after the current
        # day, buy
        s_index = 0
        profit = 0
        while s_index < len(s) - 1:
            if s[s_index] < s[s_index + 1]:
                profit += s[s_index + 1] - s[s_index]
            s_index += 1
        return profit


if __name__ == "__main__":
    s = Solution()

    assert s.max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert s.max_profit([1, 2, 3, 4, 5]) == 4
    assert s.max_profit([7, 6, 4, 3, 1]) == 0

    print("Simple test cases passed!")
