import collections
import typing


class Solution:
    def calc_equation(
        self,
        equations: typing.List[typing.List[str]],
        values: typing.List[float],
        queries: typing.List[typing.List[str]],
    ) -> typing.List[int]:
        graph = collections.defaultdict(dict)
        for (numer, denom), value in zip(equations, values):
            graph[numer][denom] = value
            graph[denom][numer] = 1 / value

        def _depth_first_search_product(
            start: str, end: str, visited: typing.Optional[typing.Set] = None
        ):
            if visited is None:
                visited = set()

            visited.add(start)

            if start == end:
                return 1.0

            for neighbor in graph[start]:
                if neighbor not in visited:
                    result = _depth_first_search_product(neighbor, end, visited)
                    return result * graph[start][neighbor]

        answers = []
        for numer, denom in queries:
            if numer not in graph or denom not in graph:
                answers.append(-1.0)
            elif numer == denom:
                answers.append(1.0)
            else:
                answers.append(_depth_first_search_product(numer, denom))

        return answers


if __name__ == "__main__":
    s = Solution()

    assert s.calc_equation(
        [['a', 'b'], ['b', 'c']],
        [2, 3],
        [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']],
    ) == [6.0, 0.5, -1.0, 1.0, -1.0]

    assert s.calc_equation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    ) == [3.75, 0.4, 5.0, 0.2]

    assert s.calc_equation(
        [["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    ) == [0.5, 2.0, -1.0, -1.0]

    print("Test cases passed!")
