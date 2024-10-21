import collections
import typing


class Solution:
    def min_mutation(self, start_gene: str, end_gene: str, bank: typing.List[str]) -> int:
        # obvious
        if end_gene not in bank:
            return -1

        # initialize objects for BFS
        queue = collections.deque([(start_gene, 1)])
        visited = set()

        mutations = ['A', 'C', 'G', 'T']

        while queue:
            start_gene, depth = queue.popleft()

            for mutation in mutations:
                for i in range(8):
                    next_gene = start_gene[:i] + mutation + start_gene[i + 1 :]
                    if next_gene not in bank:
                        continue
                    if next_gene in visited:
                        continue
                    if next_gene == end_gene:
                        return depth
                    visited.add(next_gene)
                    queue.append((next_gene, depth + 1))

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.min_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    assert s.min_mutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
    assert (
        s.min_mutation("AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"])
        == -1
    )

    print("Test cases passed!")
