import typing

import tree_utils


class Solution:
    def _get_depth(self, root: typing.Optional[tree_utils.TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth
        while root.left is not None:
            root = root.left
            depth += 1
        return depth

    def count_nodes(self, root: typing.Optional[tree_utils.TreeNode]) -> int:
        # there is a trick to this question that takes advantage of the completeness of the tree
        # and allows you to use recursion
        # if you calculate the depth of the tree by repeatedly "going left", then if the depth of
        # the right tree is less than the depth of the left tree, it must be the case that the
        # right tree is complete. In this case, we can count the number of nodes in the right tree
        # (including `root`), and then recursively call the function on the rest of the tree;
        # namely, `root.left`.
        # Conversely, if the depth of the right tree *equals* the depth of the left tree, which
        # will "typically" be true, we can add the number of nodes in the left tree (including
        # `root`) and then recursively call the function on the rest of the tree; namely,
        # `root.right`
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1

        left_depth = self._get_depth(root.left)
        right_depth = self._get_depth(root.right)

        if left_depth == right_depth:
            # the left tree is complete
            return (2 ** (left_depth + 1)) + self.count_nodes(root.right)
        else:
            # the right tree is complete
            return (2 ** (right_depth + 1)) + self.count_nodes(root.left)


if __name__ == "__main__":

    s = Solution()

    assert s.count_nodes(tree_utils.list_to_tree([1, 2, 3, 4, 5, 6])) == 6
    assert s.count_nodes(tree_utils.list_to_tree([1])) == 1
    assert s.count_nodes(tree_utils.list_to_tree([])) == 0

    print("Simple test cases passed!")
