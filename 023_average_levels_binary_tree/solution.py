import collections
import typing

import tree_utils


class Solution:
    def average_of_levels(self, root: typing.Optional[tree_utils.TreeNode]) -> typing.List[float]:
        averages = []

        queue = collections.deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                element = queue.popleft()

                level_sum += element.val

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)

            averages.append(level_sum / level_count)

        return averages


if __name__ == "__main__":
    s = Solution()

    assert s.average_of_levels(tree_utils.list_to_tree([3, 9, 20, None, None, 15, 7])) == [
        3.0,
        14.5,
        11.0,
    ]
    assert s.average_of_levels(tree_utils.list_to_tree([3, 9, 20, 15, 7])) == [3.0, 14.5, 11.0]

    print("Simple test cases passed!")
