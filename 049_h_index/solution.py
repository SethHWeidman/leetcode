import typing


class Solution:
    def h_index(self, citations: typing.List[int]) -> int:
        # idea: since the h_index can't be greater than the length of the list of `citations`:
        # first create a list where the ith element, indexed from 1, is the number of times that
        # exact number of citations appears; and in the case when the ith element is greater than
        # the length of `citations`, we simply count it as having `length(citations)` citations
        num_citations = len(citations)
        citations_list = [0] * len(citations)
        for citation in citations:
            if citation == 0:
                continue
            if citation >= num_citations:
                citations_list[num_citations - 1] += 1
            else:
                citations_list[citation - 1] += 1

        # now we can simply iterate through `citations_list` backwards, keeping track of the total
        # number of citations greater than `i` at each iteration
        tot = 0
        for i in range(num_citations, -1, -1):
            # need to be careful in this `for` loop to increment `tot` correctly and `return` at
            # the right time; remembering the definition of `citations_list` helps
            tot += citations_list[i - 1]
            if tot >= i:
                return i
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.h_index([3, 0, 6, 1, 5]) == 3
    assert s.h_index([1]) == 1
    assert s.h_index([1, 3, 1]) == 1
