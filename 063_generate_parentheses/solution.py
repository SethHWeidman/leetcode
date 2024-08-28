import typing


class Solution:
    def generate_parentheses(self, n: int) -> typing.List:
        results = []

        def _backtrack(s: str = '', left: int = 0, right: int = 0) -> None:
            if len(s) == 2 * n:
                # we have found a successful candidate string
                results.append(s)
                return

            # if we can add a left parentheses, do so:
            if left < n:
                _backtrack(s + '(', left + 1, right)

            # otherwise, if we can add a right parentheses, do so
            if right < left:
                _backtrack(s + ')', left, right + 1)

        _backtrack()

        return results


if __name__ == "__main__":
    s = Solution()

    assert s.generate_parentheses(1) == ["()"]
    assert s.generate_parentheses(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    print("Simple test cases passed!")
