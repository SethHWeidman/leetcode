import typing

from leetcode import tree_utils


class Solution(object):
    def tree_from_preorder_inorder(
        self, preorder: typing.List[int], inorder: typing.List[int]
    ) -> tree_utils.TreeNode:
        # in general, to construct a tree, we must define:
        #   * how to choose the root node
        #   * how to recursively construct the left and right branches
        #
        # Preorder traversal involves traversing:
        #   1. Root
        #   2. Left subtree
        #   3. Right subtree
        # whereas inorder traversal involves traversing:
        #   1. Left subtree
        #   2. Root
        #   3. Right subtree
        #
        # From these observations, we see that:
        # 1. We can get the root node of the tree by simply taking the first element of `preorder`
        # 2. We can get the elements of the left tree by taking:
        #   * The first "half" roughly of `preorder`
        #   * The elements of `inorder` prior to `root`
        #
        # But first, the handling of the null case:
        if not len(preorder):
            return None

        root_value = preorder[0]

        root_node = tree_utils.TreeNode(root_value)

        root_value_index = inorder.index(root_value)

        # need to reference `root_value_index + 1` in the `preorder` list because the list indices
        # are shifted by one since we've removed the first element
        root_node.left = self.tree_from_preorder_inorder(
            preorder[1 : root_value_index + 1], inorder[:root_value_index]
        )
        root_node.right = self.tree_from_preorder_inorder(
            preorder[root_value_index + 1 :], inorder[root_value_index + 1 :]
        )
        return root_node


if __name__ == '__main__':
    s = Solution()

    assert tree_utils.bst_to_list(
        s.tree_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    ) == [3, 9, 20, None, None, 15, 7]
    assert tree_utils.bst_to_list(s.tree_from_preorder_inorder([-1], [-1])) == [-1]
    print("Simple test cases passed!")
