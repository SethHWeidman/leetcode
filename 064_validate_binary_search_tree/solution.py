import tree_utils
import typing


class Solution:
    def is_valid_bst(self, root: tree_utils.TreeNode) -> bool:

        prev_val = [float('-inf')]

        def _validate_in_order(node: typing.Optional[tree_utils.TreeNode]) -> bool:
            # an empty node is valid
            if not node:
                return True

            if not _validate_in_order(node.left):
                return False

            current_value = node.val

            if not current_value > prev_val[0]:
                return False

            prev_val[0] = current_value

            return _validate_in_order(node.right)

        return _validate_in_order(root)


if __name__ == "__main__":
    s = Solution()

    assert s.is_valid_bst(tree_utils.list_to_tree([2, 1, 3]))
    assert not s.is_valid_bst(tree_utils.list_to_tree([5, 1, 4, None, None, 3, 6]))

    print("Test cases passed!")
