import heapq
import typing


class Solution:
    def k_smallest_pairs(
        self, nums1: typing.List[int], nums2: typing.List[int], k: int
    ) -> typing.List[typing.List[int]]:
        # The idea to this solution is to use a "Min-heap":
        # https://en.wikipedia.org/wiki/Heap_(data_structure)
        # The `tuple` example in the docs below is most relevant.
        # https://docs.python.org/3/library/heapq.html#basic-examples

        index_1, index_2 = 0, 0
        length_1, length_2 = len(nums1), len(nums2)

        heap_queue = [(nums1[index_1] + nums2[index_2], (index_1, index_2))]
        answer = []
        visited = set((0, 0))

        while k > 0:
            _, (index_1, index_2) = heapq.heappop(heap_queue)
            answer.append([nums1[index_1], nums2[index_2]])

            if index_1 < length_1 - 1 and (index_1 + 1, index_2) not in visited:
                index_tuple = (index_1 + 1, index_2)
                heapq.heappush(heap_queue, (nums1[index_1 + 1] + nums2[index_2], index_tuple))
                visited.add(index_tuple)
            if index_2 < length_2 - 1 and (index_1, index_2 + 1) not in visited:
                index_tuple = (index_1, index_2 + 1)
                heapq.heappush(heap_queue, (nums1[index_1] + nums2[index_2 + 1], index_tuple))
                visited.add(index_tuple)
            k -= 1
        return answer


if __name__ == "__main__":
    solution = Solution()

    assert solution.k_smallest_pairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert solution.k_smallest_pairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]
    print("Simple test cases passed!")
