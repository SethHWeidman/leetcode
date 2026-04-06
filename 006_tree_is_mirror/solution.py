import tree_utils


class Solution:
    def is_symmetric(self, root: tree_utils.TreeNode | None) -> bool:
        def _trees_equal(
            root1: tree_utils.TreeNode | None, root2: tree_utils.TreeNode | None
        ) -> bool:
            # the trick here is to create a filpp

            # handle null cases
            if not root1 and not root2:
                return True
            elif root1 and not root2:
                return False
            elif not root1 and root2:
                return False

            return (
                root1.val == root2.val
                and _trees_equal(root1.left, root2.right)
                and _trees_equal(root1.right, root2.left)
            )

        return _trees_equal(root, root)


if __name__ == "__main__":

    s = Solution()

    assert s.is_symmetric(tree_utils.list_to_tree([1, 2, 2, 3, 4, 4, 3]))

    print("Simple test case passed!")
