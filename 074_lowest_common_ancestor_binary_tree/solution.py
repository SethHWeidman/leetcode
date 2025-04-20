import typing

import tree_utils


class Solution:
    def lowest_common_ancestor(
        self, root: typing.Optional[tree_utils.TreeNode], p: int, q: int
    ) -> tree_utils.TreeNode:
        if not root:
            return None

        if root.val == p or root.val == q:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


if __name__ == "__main__":
    s = Solution()

    assert (
        s.lowest_common_ancestor(
            tree_utils.list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 1
        ).val
        == 3
    )
    assert (
        s.lowest_common_ancestor(
            tree_utils.list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 4
        ).val
        == 5
    )
    assert (
        s.lowest_common_ancestor(
            tree_utils.list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 6, 4
        ).val
        == 5
    )

    print("Test cases passed!")
