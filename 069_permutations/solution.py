import typing


class Solution:
    def permutations(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:

        results = []

        def _backtrack(current: typing.List[int], remaining: typing.List[int]) -> None:
            if not remaining:
                results.append(current[:])  # `results.append(current)` will not work!
                return

            for i, num in enumerate(remaining):
                current.append(num)
                _backtrack(current, remaining[:i] + remaining[i + 1 :])
                current.pop()

        _backtrack([], nums)
        return results


if __name__ == "__main__":
    s = Solution()

    assert s.permutations([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert s.permutations([0, 1]) == [[0, 1], [1, 0]]
    assert s.permutations([1]) == [[1]]

    print("Simple test cases passed!")
