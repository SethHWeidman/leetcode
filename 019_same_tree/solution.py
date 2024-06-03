import typing

import tree_utils


class Solution:
    def is_same_tree(
        self, p: typing.Optional[tree_utils.TreeNode], q: typing.Optional[tree_utils.TreeNode]
    ) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            # and, implicitly, from the lines above, they are not both `None`
            return False
        if p.val != q.val:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()

    assert s.is_same_tree(tree_utils.list_to_tree([1, 2, 3]), tree_utils.list_to_tree([1, 2, 3]))
    assert not s.is_same_tree(
        tree_utils.list_to_tree([1, 2]), tree_utils.list_to_tree([1, None, 2])
    )
    assert not s.is_same_tree(
        tree_utils.list_to_tree([1, 2, 1]), tree_utils.list_to_tree([1, 1, 2])
    )

    print("Simple test cases passed!")
